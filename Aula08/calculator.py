class Calculator:
    def add(self, a: float, b: float) -> float:
        """
        Adiciona dois números.
        
        Args:
            a: Primeiro número
            b: Segundo número
            
        Returns:
            A soma dos dois números
        """
        return a + b
    
    def subtract(self, a: float, b: float) -> float:
        """
        Subtrai o segundo número do primeiro.
        
        Args:
            a: Primeiro número
            b: Segundo número
            
        Returns:
            A diferença entre os dois números
        """
        return a - b
    
    def multiply(self, a: float, b: float) -> float:
        """
        Multiplica dois números.
        
        Args:
            a: Primeiro número
            b: Segundo número
            
        Returns:
            O produto dos dois números
        """
        return a * b
    
    def divide(self, a: float, b: float) -> float:
        """
        Divide o primeiro número pelo segundo.
        
        Args:
            a: Primeiro número (dividendo)
            b: Segundo número (divisor)
            
        Returns:
            O quociente da divisão
            
        Raises:
            ZeroDivisionError: Se o divisor for zero
        """
        if b == 0:
            raise ZeroDivisionError("Não é possível dividir por zero")
        return a / b
    
    def power(self, base: float, exponent: float) -> float:
        """
        Calcula a potência de um número.
        
        Args:
            base: A base
            exponent: O expoente
            
        Returns:
            A base elevada ao expoente
        """
        return base ** exponent
    
    def factorial(self, n: int) -> int:
        """
        Calcula o fatorial de um número.
        
        Args:
            n: O número para calcular o fatorial
            
        Returns:
            O fatorial do número
            
        Raises:
            ValueError: Se o número for negativo
        """
        if n < 0:
            raise ValueError("Não é possível calcular fatorial de número negativo")
        if n == 0 or n == 1:
            return 1
        return n * self.factorial(n - 1) 