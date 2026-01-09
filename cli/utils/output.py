from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()


def banner(title, subtitle=""):
    console.print(
        Panel(
            f"[bold cyan]{title}[/bold cyan]\n[dim]{subtitle}[/dim]",
            expand=False,
        )
    )


def module_result(result: dict):
    table = Table(
        title=f"[bold]{result.get('module', 'UNKNOWN')}[/bold]",
        header_style="bold magenta",
    )

    table.add_column("Campo", style="cyan")
    table.add_column("Valor", style="white")

    table.add_row("Categoría", str(result.get("category")))
    table.add_row("Estado", _status(result.get("status")))
    table.add_row("Tiempo (s)", str(result.get("execution_time")))

    if result.get("status") == "success":
        data = result.get("data", {})
        table.add_row("Datos", _pretty(data))
    else:
        table.add_row("Error", str(result.get("error")))

    console.print(table)


def _status(status):
    if status == "success":
        return "[green]SUCCESS[/green]"
    if status == "error":
        return "[red]ERROR[/red]"
    return "[yellow]UNKNOWN[/yellow]"


def _pretty(data):
    if isinstance(data, dict):
        return "\n".join(f"{k}: {v}" for k, v in data.items())
    return str(data)
