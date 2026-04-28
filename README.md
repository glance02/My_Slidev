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

Learn more about Slidev at the [documentation](https://sli.dev/).
