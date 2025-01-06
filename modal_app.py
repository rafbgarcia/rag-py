import modal

app = modal.App("rag")

image = (
    modal.Image.debian_slim()
    .pip_install(
        "accelerate",
        "beautifulsoup4",
        "commonmark",
        "dspy-ai==2.5.43",
        "fastapi[standard]",
        "lancedb",
        "markdown-it-py",
        "markdownify",
        "sentence-transformers",
        "tantivy",
        "torch",
        "transformers",
        "cloudpickle",
    )
    .copy_local_dir("./routers", "/root/routers")
    .copy_local_dir("./utils", "/root/utils")
    .add_local_dir("./data/docs", "/root/data/docs")
)


@app.cls(
    image=image,
    memory=4096,
    cpu=2.0,
    secrets=[modal.Secret.from_name("openai-secret")],
)
class ModalApp:
    @modal.enter()
    def imports(self):
        from routers.model import Model

        self.program = Model().activate_assertions()

    @modal.web_endpoint(method="POST")
    def qa(self, params: dict):
        import dspy

        pred = self.program(messages=params.get("messages"))

        dspy.inspect_history(1)

        return {"text": pred.response}
