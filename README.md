# Welcome to [Slidev](https://github.com/slidevjs/slidev)!

To start the slide show:

- `pnpm install`
- `pnpm dev`
- visit <http://localhost:3030>

Edit the [slides.md](./slides.md) to see the changes.

## Run Python code blocks

This project supports local Python execution for Slidev Monaco runner blocks:

````md
```python {monaco-run} {autorun:false}
print("Hello, Slidev!")
```
````

Start the runner from the mamba environment you want to use:

```powershell
mamba activate <env-name>
python tools/slidev_python_runner.py
```

Then start Slidev in another terminal:

```powershell
pnpm dev
```

The runner listens on `127.0.0.1:8765` by default and is intended for trusted local code only.

For remote access through frp, proxy only the Slidev port, for example local `3030` to your public frp URL. The browser calls `/python-runner/run` on the Slidev site, and the local Slidev dev server forwards that request to `127.0.0.1:8765`.

```powershell
python tools/slidev_python_runner.py
pnpm dev
```

This keeps the Python runner bound to the local machine, but anyone who can access the frp Slidev URL can still trigger code execution through the page. Use it only on a trusted or access-controlled URL.

Learn more about Slidev at the [documentation](https://sli.dev/).
