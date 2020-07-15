// Nota: la primera linea debe contener el nombre del paquete: package nombre_paquete;
import javax.swing.JOptionPane;

public class HolaMundo {
    
    // Metodo principal (main) del programa 
    public static void main(final String[] args) 
    {
        // Impresion por consola:
        System.out.println("Hola Mundo");
        // Impresion por ventana emergente
        JOptionPane.showMessageDialog(null, "Hola Mundo");
	}
}