        <template>
                <div class=" ">

                        <div class="container p-4">
                        <div class="cargando">
                        <div class="pelotas"></div>
                        <div class="pelotas"></div>
                        <div class="pelotas"></div>
                        <span class="texto-cargando">Cargando...</span>
                        </div>
                </div>
                <!-- Botón para salir y volver al menú -->
                <button @click="irAlMenu" class="btn btn-danger p-2 mt-2">
                        <i class="fas fa-arrow-left"></i> Salir al Menú
                </button>
                <h1 class="text-center p-4">Página en mantenimiento <i class="fa-solid fa-face-sad-tear fa-bounce"></i></h1>
                </div>
        
                <div class="d-flex flex-column align-items-center justify-content-center  text-center">
                <!-- Botón para mostrar/ocultar mensaje -->
                <button 
                @click="mostrarMensaje = !mostrarMensaje" 
                class="btn btn-primary mb-3"
                >
                {{ mostrarMensaje ? "Ocultar Mensaje" : "Mostrar Mensaje" }}
                </button>
        
                <!-- Mensaje de mantenimiento -->
                <h2 v-if="mostrarMensaje" class="p-4 mt-4 alert alert-warning">
                En poco estará en funcionamiento, gracias por su paciencia...
                </h2>
        
                </div>
        </template>
        
        <script>
        export default {
                data() {
                return {
                mostrarMensaje: false,
                };
                },
                methods: {
                irAlMenu() {
                
                this.$router.push('/menu'); // Si usas Vue Router
                // window.location.href = "/ruta-del-menu"; // Alternativa sin Vue Router
                }
                }
        };
        </script>
        
        <style scoped>
        /* Puedes agregar estilos adicionales aquí */
        @import url('//fonts.googleapis.com/css2?family=Montserrat:ital,wght@1,800&display=swap');

body{
    font-family: 'Montserrat', sans-serif;
  font-weight: 800;
    background-color: #434343;
    color: #00b8de;
}
/* ======================== */
.container{   
  display: grid;
    place-content: center;
}
.cargando{
    width: 120px;
    height: 30px;
    display: flex;
    flex-wrap: wrap;
    align-items: flex-end;
    justify-content: space-between;
  margin: 0 auto; 
}
.texto-cargando{ 
  padding-top:20px
}
.cargando span{
    font-size: 20px;
    text-transform: uppercase;
}
.pelotas {
    width: 30px;
    height: 30px;
    background-color: #00b8de;
    animation: salto .5s alternate
    infinite;
  border-radius: 50%  
}
.pelotas:nth-child(2) {
    animation-delay: .18s;
}
.pelotas:nth-child(3) {
    animation-delay: .37s;
}
@keyframes salto {
    from {
        transform: scaleX(1.25);
    }
    to{
        transform: 
        translateY(-50px) scaleX(1);
    }
}
        </style>
        