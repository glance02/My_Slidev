#!/usr/bin/env python
"""Local Python runner for Slidev Monaco code blocks.

Start this file from the mamba environment you want Slidev to use:

    mamba activate <env-name>
    python tools/slidev_python_runner.py

The server intentionally binds to 127.0.0.1 only. It executes trusted local
code sent by your Slidev browser tab. If the slides are exposed through frp,
let the Slidev dev server proxy /python-runner/run to this local runner.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any


DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 8765
DEFAULT_TIMEOUT_SECONDS = 10.0
MAX_BODY_BYTES = 256 * 1024


class PythonRunnerHandler(BaseHTTPRequestHandler):
    server_version = "SlidevPythonRunner/1.0"

    def do_OPTIONS(self) -> None:
        self._send_empty(204)

    def do_GET(self) -> None:
        if self.path == "/health":
            self._send_json(
                200,
                {
                    "ok": True,
                    "python": sys.executable,
                    "version": sys.version,
                },
            )
            return

        self._send_json(404, {"ok": False, "error": "Not found"})

    def do_POST(self) -> None:
        if self.path != "/run":
            self._send_json(404, {"ok": False, "error": "Not found"})
            return

        payload = self._read_json_body()
        if payload is None:
            return

        code = payload.get("code")
        if not isinstance(code, str):
            self._send_json(400, {"ok": False, "error": "Expected JSON body with a string 'code' field."})
            return

        timeout = self._coerce_timeout(payload.get("timeout"))

        try:
            completed = subprocess.run(
                [sys.executable, "-c", code],
                capture_output=True,
                check=False,
                encoding="utf-8",
                env={**os.environ, "PYTHONIOENCODING": "utf-8"},
                errors="replace",
                text=True,
                timeout=timeout,
            )
        except subprocess.TimeoutExpired as error:
            self._send_json(
                200,
                {
                    "ok": False,
                    "timedOut": True,
                    "exitCode": None,
                    "stdout": error.stdout or "",
                    "stderr": f"Python execution timed out after {timeout:g} seconds.",
                },
            )
            return

        self._send_json(
            200,
            {
                "ok": completed.returncode == 0,
                "timedOut": False,
                "exitCode": completed.returncode,
                "stdout": completed.stdout,
                "stderr": completed.stderr,
                "python": sys.executable,
            },
        )

    def log_message(self, format: str, *args: Any) -> None:
        sys.stderr.write("%s - %s\n" % (self.address_string(), format % args))

    def _read_json_body(self) -> dict[str, Any] | None:
        content_length = self.headers.get("Content-Length")
        if content_length is None:
            self._send_json(411, {"ok": False, "error": "Missing Content-Length header."})
            return None

        try:
            length = int(content_length)
        except ValueError:
            self._send_json(400, {"ok": False, "error": "Invalid Content-Length header."})
            return None

        if length > MAX_BODY_BYTES:
            self._send_json(413, {"ok": False, "error": "Request body is too large."})
            return None

        try:
            raw_body = self.rfile.read(length)
            payload = json.loads(raw_body.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            self._send_json(400, {"ok": False, "error": "Request body must be valid UTF-8 JSON."})
            return None

        if not isinstance(payload, dict):
            self._send_json(400, {"ok": False, "error": "Request body must be a JSON object."})
            return None

        return payload

    def _coerce_timeout(self, value: Any) -> float:
        if isinstance(value, (int, float)) and value > 0:
            return min(float(value), 120.0)
        return self.server.timeout_seconds  # type: ignore[attr-defined]

    def _send_empty(self, status: int) -> None:
        self.send_response(status)
        self._send_common_headers()
        self.end_headers()

    def _send_json(self, status: int, payload: dict[str, Any]) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self._send_common_headers()
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_common_headers(self) -> None:
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run Python code for Slidev Monaco blocks.")
    parser.add_argument("--host", default=DEFAULT_HOST, help=f"Bind host. Default: {DEFAULT_HOST}")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT, help=f"Bind port. Default: {DEFAULT_PORT}")
    parser.add_argument(
        "--timeout",
        type=float,
        default=DEFAULT_TIMEOUT_SECONDS,
        help=f"Default execution timeout in seconds. Default: {DEFAULT_TIMEOUT_SECONDS:g}",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    server = ThreadingHTTPServer((args.host, args.port), PythonRunnerHandler)
    server.timeout_seconds = max(args.timeout, 0.1)

    print(f"Slidev Python runner listening at http://{args.host}:{args.port}")
    print(f"Python executable: {sys.executable}")
    print("Press Ctrl+C to stop.")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping Slidev Python runner.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
