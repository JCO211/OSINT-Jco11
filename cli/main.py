import asyncio
import typer

from core.engine import OsintEngine
from core.plugin_loader import load_modules
from core.utils.target import normalize_target
from modules import infrastructure
from cli.utils.output import banner, module_result
from rich.console import Console

console = Console()

app = typer.Typer(help="OSINT Jco11 - Toolkit OSINT pasivo y modular")
scan_app = typer.Typer(help="Ejecutar escaneos OSINT")
app.add_typer(scan_app, name="scan")


@scan_app.command("run")
def scan_run(
    target: str = typer.Option(..., "--target", "-t"),
    target_type: str = typer.Option(..., "--type"),
):
    banner("OSINT Jco11", f"Target: {target}\n({target_type})")

    engine = OsintEngine()

    for module in load_modules(infrastructure):
        engine.register_module(module)

    normalized = normalize_target(target, target_type)

    try:
        results = asyncio.run(engine.run(normalized))
    except Exception as e:
        console.print(f"[bold red]Error crítico:[/bold red] {e}")
        raise typer.Exit(1)

    if not results:
        console.print(
            "[bold yellow][!] No hay módulos compatibles con este tipo de target[/bold yellow]"
        )
        return

    for result in results:
        module_result(result)

    banner("OSINT Jco11", "Scan finalizado")


if __name__ == "__main__":
    app()
