import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class MiServlet extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        
        // Obtener parámetros de la solicitud
        String parametro = request.getParameter("nombreDelParametro");
        
        // Procesar la solicitud
        // ...

        // Crear una respuesta
        response.setContentType("text/html");
        response.getWriter().println("<h1>Respuesta del Servlet</h1>");
        response.getWriter().println("<p>El valor del parámetro es: " + parametro + "</p>");
    }
    
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        
        // Obtener parámetros del formulario
        String nombre = request.getParameter("nombre");
        String apellido = request.getParameter("apellido");
        
        // Procesar la solicitud
        // ...
        
        // Utilizar JSP para crear una página dinámica
        request.setAttribute("nombreCompleto", nombre + " " + apellido);
        request.getRequestDispatcher("/saludo.jsp").forward(request, response);
    }
}
