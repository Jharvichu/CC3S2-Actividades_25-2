# Implementa la función summarize y el CLI.
# Requisitos:
# - summarize(nums) -> dict con claves: count, sum, avg
# - Valida que nums sea lista no vacía y elementos numéricos (acepta strings convertibles a float).
# - CLI: python -m app "1,2,3" imprime: sum=6.0 avg=2.0 count=3

def summarize(nums):  # TODO: tipado opcional
    """
    Calcula estadísticas de una lista de números.
    
    Args:
        nums: Lista de números o strings convertibles a float
        
    Returns:
        dict con claves 'count', 'sum', 'avg'
        
    Raises:
        ValueError: Si la lista está vacía o contiene elementos no numéricos
    """
    if not isinstance(nums, list):
        raise ValueError("nums debe ser una lista")
    
    if not nums:
        raise ValueError("La lista no puede estar vacía")
    
    # Convertir elementos a float y validar
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
