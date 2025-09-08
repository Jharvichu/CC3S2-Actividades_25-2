# Prueba de entrada - CC3S2

## Seccion 1

### Reportes

En la seccion 1 se explica cada reporte generado por el script `syscheck.sh` en los mismos reportes ubicados en la carpeta `reports`. De igual manera se menciona lo que se explico en cada reporte a continuación:

#### dns.txt
> **Explicación**
> 
> **Registro A**
>
> El **DNS** traduce el nombre del dominio (**example.com**) con una dirección **IPv4** para conectarse al servidor. El número **155** representa el **TTL (Time To Live)** en segundos, es decir, que los servidores DNS y la computadora pueden guardar esta información en caché por 155 segundos antes de volver a consultar. **IN** representa la clase del registro (**internet**). Además, hay varias IP para que se distribuya el tráfico y se evite la saturación (**balanceo de carga**).
>
> **Registro AAAA**
>
> El **DNS** traduce el nombre del dominio (**example.com**) con una dirección **IPv6** para conectarse al servidor, ya que IPv4 se está agotando y **IPv6** permite más direcciones únicas. El número **295** representa el **TTL (Time To Live)** en segundos, es decir, que los servidores DNS y la computadora pueden guardar esta información en caché por 295 segundos antes de volver a consultar.  **IN** representa la clase del registro (**internet**). Además, hay varias IP para que se distribuya el tráfico y se evite la saturación (**balanceo de carga**).
>
> **Registro MX**
>
> Este registro indica los servidores de correo responsables de recibir emails para **example.com**. El número **0** define la prioridad (**0 es la más alta**).  El número **84170** es el **TTL** en segundos, expresa un valor alto para evitar cambios frecuentes y reducir la carga en los servidores DNS.
>
> **Nota:**  
> Observamos que los **TTL** difieren:  
> - Un **TTL alto** nos trae ventajas como menos consultas DNS (menos carga en los servidores y más rápido para los usuarios). Sin embargo, si cambiamos de IP o servidor de correo, se demoraría mucho tiempo en reflejar el cambio.  
> - Un **TTL bajo** hace que los cambios en DNS sean más rápidos, pero al haber más consultas DNS, habría más carga en los servidores.


#### dns.txt
> **Explicación:**
> 
> - **HTTP/2** es la versión del protocolo HTTP que estamos utilizando, un protocolo que es más rápido y eficiente que su predecesor HTTP/1.1, 
>   ya que permite la multiplexación, compresión de headers y priorización de recursos.  
>   El número **200** es el código de HTTP que significa **OK** y que indica que la solicitud del cliente (nosotros) fue exitosa y el servidor respondió correctamente.
>
> - **text/html** es el contenido que el servidor está enviando al cliente (nosotros), en este caso es un **HTML**.
>
> - `"84238dfc8092e5d9c0dac8ef93371a07:1736799080.121134"` es el identificador de un recurso para una versión específica del recurso, sirve
>   para validar si un recurso ha cambiado. Si el **ETag** no cambia, se puede utilizar la versión en caché para no descargar nuevamente el recurso.
>
> - **Mon, 13 Jan 2025 20:11:20 GMT** es la fecha de la última modificación del recurso y junto con el **ETag** sirve para decidir si descargar un
>   recurso nuevamente o usar la versión en caché.
>
> - **max-age=86000** aquí nos indican el tiempo (**86000s**) en que el navegador no solicitará el recurso al servidor, sino que usará la versión local.
>
> - **Sun, 07 Sep 2025 03:59:26 GMT** esta es la fecha en que se generó la respuesta del servidor.
>
> - **h3=":443"; ma=93600,h3-29=":443"; ma=93600** aquí nos indican que el servidor soporta **HTTP/3** en el puerto **443**, y que además la información en
>   la caché se queda **93600s**.

#### sockets.txt
> **Explicación**
> 
> En la primera línea se muestra el comando que permite visualizar estadísticas de **sockets**, acompañado de las siguientes *flags*:
> - **-t**: Muestra solo sockets **TCP**.
> - **-u**: Muestra solo sockets **UDP**.
> - **-l**: Muestra solo sockets en estado de escucha (**LISTEN**).
> - **-n**: Muestra direcciones IP y puertos en formato numérico.
>
> En la tabla se muestran las siguientes columnas:
> - **Netid**: Tipo de sockets.
> - **State**: Indica si está en estado **LISTEN** (escucha) o **UNCONN** (sin conexión).
> - **Recv-Q**: Bytes recibidos pero no procesados.
> - **Send-Q**: Bytes enviados pero no confirmados.
> - **Local Address:Port**: Dirección IP y puerto local donde el socket está escuchando.
> - **Peer Address:Port**: Dirección IP y puerto remoto (en este caso `0.0.0.0:*` o `[::]:*` significa cualquier dirección).
> - **Process**: Proceso asociado al socket.
>
> **Riesgos**  
> Mantener puertos abiertos innecesarios puede generar varios riesgos:
> - **Ataques de fuerza bruta**: si hay un puerto expuesto, un atacante puede intentar adivinar contraseñas.
> - **Explotación de vulnerabilidades**: servicios desactualizados pueden tener fallos conocidos.
> - **Consumo de recursos**: un puerto abierto puede ocasionar uso excesivo de recursos del sistema.

### Makefile

En el makefile se realizo pocos cambios, solamente se puso una condicional que verifica que si una herramienta no esta instalada te imprima un mensaje y continue verificando las otras herramientas.

```Makefile
SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c

.PHONY: help tools report all
help: ## Mostrar ayuda
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | sed 's/:.*##/: /'

tools: ## Verifica binarios requeridos
	@echo "Verificando herramientas requeridas..."
	@for b in git bash make python3 pytest curl dig ss jq; do \
	  if ! command -v $$b >/dev/null; then \
	    echo "  Falta: $$b"; \
	  fi; \
	done
	@echo "OK herramientas restantes"

report: ## Genera reportes HTTP/DNS/TLS/puertos
	@echo "Generando reportes..."
	@bash scripts/syscheck.sh

all: tools report ## Ejecuta todo
```

## Seccion 2

En la seccion 2 se completo la funcion de Summarize para un lista y el main, que permita el uso de a consola para el input de la lista.

```python
def summarize(nums):

    if not isinstance(nums, list):
        raise ValueError("nums debe ser una lista")
    
    if not nums:
        raise ValueError("La lista no puede estar vacía")
    
    converted_nums = []
    for item in nums:
        try:
            converted_nums.append(float(item))
        except (ValueError, TypeError):
            raise ValueError(f"Elementos no numéricos encontrado: {item}")
    
    total = sum(converted_nums)
    count = len(converted_nums)
    avg = total / count
    
    return {
        'count': count,
        'sum': total,
        'avg': avg
    }


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Comando de uso: python -m app \"1,2,3\"")
        sys.exit(1)
    
    raw = sys.argv[1]
    items = [p.strip() for p in raw.split(",") if p.strip()]
    
    try:
        result = summarize(items)
        print(f"sum={result['sum']} avg={result['avg']} count={result['count']}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
```

Ademas se realizo solamente el test de la funcion Summarize, como se presenta a continuación.

```python
import pytest
from app.app import summarize

@pytest.fixture
def sample():
    return ["1", "2", "3"]

def test_ok(sample):
    # Act
    result = summarize(sample)
    
    # Assert
    assert result == {'count': 3, 'sum': 6.0, 'avg': 2.0}
    assert isinstance(result, dict)
    assert 'count' in result and 'sum' in result and 'avg' in result

def test_empty():
    with pytest.raises(ValueError, match="La lista no puede estar vacía"):
        summarize([])

def test_not_a_list():
    with pytest.raises(ValueError, match="nums debe ser una lista"):
        summarize("not a list")

def test_non_numeric():
    with pytest.raises(ValueError, match="Elementos no numéricos encontrado"):
        summarize(["a", "2"])
```

Se procedio a ejecutar las pruebas, escribimos el siguiente comando:

``` bash
# Debemos ubicarnos en seccion2_python_git
PYTHONPATH=. pytest 

# Para generar un reporte de la cobertura en coverage.txt ejecutamos el siguiente comando
PYTHONPATH=. pytest --cov=app --cov-report=term-missing tests/ > coverage.txt
```

Respecto al uso de git, se ejecuto los siguientes comandos para validar el uso de rebase, merge ff, y cherry-pick

``` bash
git add .
git commit -m "Implementacion de la función summarize y CLI"

# Creamos una nueva ramma un hacemos un commit
git checkout -b feature/msg
git add .
git commit -m "Mejorar mensajes de usuario en CLI"

# Mergeamos y este seria un FF
git checkout main
git merge feature/msg

# Hacemos un fix específico
git checkout -b hotfix/validation
git add .
git commit -m "Fix: validación de entrada"
git checkout main
git cherry-pick hotfix/validation # Tomamos solo ese commit específico

# Rebase en otra rama
git checkout -b feature/improvements
git add .
git commit -m "Agregar documentación a summarize"
git commit -m "Mejorar mensaje de usuario en CLI"
git checkout main
# Hacemos un commit en main para crear divergencia
git add . 
git commit -m "Readme inicial de la PE"
git checkout feature/improvements
git rebase main  # Rebase los commits sobre main
git checkout main
git merge feature/improvements # Merge limpio después del rebase

# Escribimos todo lo modificado en git_log.txt
git log --oneline --graph --all > git_log.txt
```

## Seccion 3

Se procedio a explicar los conceptos que nos piden en esta seccion en `network_answer.txt` y `deploy_scenario.txt`.

## Reproducción

```bash
# Ubuntu/WSL
cd Prueba_entrada_CC3S2/
python3 -m venv venv
source venv/bin/activate
pip pytest pytest-cov

# Sección 1
cd seccion1_cli_automatizacion
make all # Lo comentarios en los reportes/ se borraran
cd ..

# Sección 2
cd seccion2_python_git/app
python3 -m app "1,2,3"
cd ..
PYTHONPATH=. pytest 
cd ..

# Sección 3
cd seccion3_redes_api/
curl -s https://example.com -o example.html
dig google.com * +noall +answer > dig_output.txt
curl -s https://jsonplaceholder.typicode.com/posts/1 -o api_response.json
jq -r '.title' api_response.json > api_title.txt
```
