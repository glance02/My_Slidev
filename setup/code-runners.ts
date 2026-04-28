import { defineCodeRunnersSetup } from '@slidev/types'

type PythonRunnerResponse = {
  ok: boolean
  timedOut?: boolean
  exitCode?: number | null
  stdout?: string
  stderr?: string
  python?: string
  error?: string
}

const DEFAULT_ENDPOINT = 'http://127.0.0.1:8765/run'
const DEFAULT_TIMEOUT_SECONDS = 10

function optionString(value: unknown, fallback: string): string {
  return typeof value === 'string' && value.length > 0 ? value : fallback
}

function optionNumber(value: unknown, fallback: number): number {
  return typeof value === 'number' && Number.isFinite(value) && value > 0 ? value : fallback
}

function formatOutput(result: PythonRunnerResponse): string {
  const output = [result.stdout, result.stderr].filter(Boolean).join('\n')

  if (output.length > 0)
    return output

  if (result.ok)
    return ''

  if (result.error)
    return result.error

  if (typeof result.exitCode === 'number')
    return `Python process exited with code ${result.exitCode}.`

  return 'Python execution failed.'
}

function escapeHtml(value: string): string {
  return value
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;')
}

function formatPreOutput(text: string, ok: boolean): string {
  const color = ok ? 'inherit' : '#f87171'

  return `<pre style="margin:0;white-space:pre-wrap;font:inherit;line-height:inherit;color:${color};">${escapeHtml(text)}</pre>`
}

export default defineCodeRunnersSetup(() => {
  async function runPython(code: string, ctx: { options: Record<string, unknown> }) {
    const endpoint = optionString(ctx.options.endpoint, DEFAULT_ENDPOINT)
    const timeout = optionNumber(ctx.options.timeout, DEFAULT_TIMEOUT_SECONDS)

    try {
      const response = await fetch(endpoint, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ code, timeout }),
      })

      if (!response.ok) {
        return {
          error: `Python runner returned HTTP ${response.status}. Is tools/slidev_python_runner.py running?`,
        }
      }

      const result = await response.json() as PythonRunnerResponse
      const text = formatOutput(result)

      if (!result.ok) {
        return {
          html: formatPreOutput(text, false),
        }
      }

      return {
        html: formatPreOutput(text, true),
      }
    }
    catch (error) {
      return {
        error: `Cannot reach the local Python runner at ${endpoint}. Start it with: python tools/slidev_python_runner.py`,
      }
    }
  }

  return {
    python: runPython,
  }
})
