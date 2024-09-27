class Book:    
    def __init__(self,title):
        self.title = title
        self.is_available = True

    def mark_as_borrowed(self):
        """ 
        Verifica si el libro está disponible para pedir prestado
        Args: 
            Recibe objeto libro para alterar el estado de disponibilidad
        """
        if self.is_available:
            self.is_available=False
            return f"You have borrowed '{self.title}'"
        else:
            return (f"Sorry, {self.title} is not available in the library.")   
    def mark_as_returned(self):
        if not self.is_available:
            self.is_available=True
            return f"Thanks for returning '{self.title}'"
        else:
            return f"{self.title} is already available"