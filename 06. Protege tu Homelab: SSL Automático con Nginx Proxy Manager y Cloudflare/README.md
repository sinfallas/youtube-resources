# Protege tu Homelab: SSL Automático con Nginx Proxy Manager y Cloudflare

URL del video en Youtube: https://youtu.be/vw2HaE3F7_w

# Guía: Crear Token en Cloudflare y configurar SSL en Nginx Proxy Manager

## Fase 1: Creación del Token en Cloudflare

1. Inicia sesión en tu cuenta de Cloudflare.
2. En la esquina superior derecha, haz clic en el ícono de tu usuario y selecciona **My Profile** (Mi perfil).
3. En el menú lateral izquierdo, selecciona **API Tokens**.
4. Haz clic en el botón azul **Create Token**.
5. En la lista de plantillas, busca **Edit zone DNS** (Editar DNS de zona) y haz clic en **Use template**.
6. En la sección *Permissions* (Permisos), verifica que la configuración sea exactamente esta:
   - `Zone` | `DNS` | `Edit`
7. En la sección *Zone Resources*, restringe el uso del token a tu dominio específico por seguridad:
   - `Include` | `Specific zone` | `[Selecciona tu dominio aquí]`
8. Haz clic en **Continue to summary** y después en **Create Token**.
9. **MUY IMPORTANTE:** Copia la cadena alfanumérica del token y guárdala en un lugar seguro. Cloudflare no te la volverá a mostrar.

---

## Fase 2: Configuración en Nginx Proxy Manager

1. Accede al panel de administración de Nginx Proxy Manager.
2. Ve a la sección **SSL Certificates** en el menú de navegación.
3. Haz clic en el botón **Add SSL Certificate**.
4. En el campo *Domain Names*, escribe tu dominio (ej. `tudominio.com`). Si deseas un certificado comodín, presiona enter y añade también `*.tudominio.com`.
5. Activa el interruptor que dice **Use a DNS Challenge**.
6. En el campo *DNS Provider*, selecciona **Cloudflare** en la lista desplegable.
7. En el cuadro de texto inferior (*Credentials File Content*), elimina el texto que aparece por defecto e ingresa esta única línea de configuración (reemplazando con tu token):
   
   `dns_cloudflare_api_token=TU_TOKEN_PEGADO_AQUI`

8. Asegúrate de que el campo de correo electrónico (*Email Address*) tenga un correo válido.
9. Marca la casilla **I Agree to the Let's Encrypt Terms of Service**.
10. Haz clic en **Save**. Nginx Proxy Manager validará el dominio creando un registro TXT temporal en Cloudflare y emitirá tu certificado SSL automáticamente.
