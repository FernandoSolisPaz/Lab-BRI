<template>
    <main class="news-view">
        <v-container>
            <!-- Article Content -->
            <v-card flat color="white" elevation="4">
                <v-card-text class="pa-6">
                    <!-- Back Button and Title -->
                    <div class="d-flex align-center mb-4">
                        <v-btn icon variant="text" size="small" class="mr-3" @click="goBack">
                            <v-icon>mdi-arrow-left</v-icon>
                        </v-btn>
                        
                        <!-- Verificar si noticia.value existe -->
                        <h1 v-if="noticia" class="text-h4 font-weight-bold flex-grow-1">{{ noticia.titulo }}</h1>
                        <div v-if="noticia" class="mb-4" style="text-align: center;">
                            <v-img v-if="noticia" :src="getLogo(noticia.pagina || 'default')" style="width: 80px; height: 80px; object-fit: contain;"/>
                            <a v-if="noticia" :href="noticia.hipervinculo" class="text-blue" target="_blank">Link de la noticia</a>
                        </div>
                    </div>

                    <!-- Article Content -->
                    <div v-if="noticia" class="mb-6">
                        <p class="text-body-1 mb-4">{{ noticia.texto }}</p>
                    </div>

                    <!-- Article Image -->
                    <div v-if="noticia" class="mb-4" style="text-align: center;">
                        <!-- Imagen -->
                        <v-img 
                        v-if="noticia" 
                        :src="noticia.imagen" 
                        alt="Imagen de la noticia" 
                        style="max-width: 60%; height: auto; object-fit: contain; margin: 0 auto;">
                            <template v-slot:placeholder>
                                <div class="d-flex align-center justify-center fill-height">
                                    <v-progress-circular color="grey-lighten-4" indeterminate></v-progress-circular>
                                </div>
                            </template>
                        </v-img>

                        <!-- Pie de imagen -->
                        <p class="text-caption text-grey-darken-1 mt-2" style="margin-top: 10px;">{{ noticia.titulo }} - {{ noticia.pagina }}</p>
                    </div>

                    <!-- Additional Article Content -->
                    <div v-if="noticia" class="mb-4">
                        Autores: 
                        <p class="text-body-1">{{ noticia.autores.join(", ") }}</p>
                    </div>

                    <!-- Source Badge -->
                    <v-chip color="orange" text-color="white" size="small" class="mt-2">Fuente noticia</v-chip>
                </v-card-text>
            </v-card>
        </v-container>
    </main>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { getLogo } from '../utils/logos';
import { toRaw } from 'vue';

interface Noticia {
        titulo: string;
        fecha_extraccion: number;
        fecha_publicacion: number;
        keywords: string[];
        pagina: string;
        hipervinculo: string;
        texto: string;
        autores: string[];
        ubicacion: string;
        imagen: string;
}

const router = useRouter();

// Variables para almacenar los datos de la noticia
const noticia = ref<Noticia | null>(null);

// Cargar la noticia desde localStorage al montar el componente
onMounted(() => {
    const noticiaData = localStorage.getItem('noticiaSeleccionada');
    if (noticiaData) {
        const noticiaParsed = JSON.parse(noticiaData);
        noticia.value = noticiaParsed;  // Aquí ya no necesitas "document"

        console.log("Noticia cargada desde localStorage: ", noticia.value);
    } else {
        console.log("No se encontraron datos en localStorage");
    }

    // Accede directamente a los datos, ya no hay "document"
    if (noticia.value) {
        console.log("Título de la noticia: ", noticia.value.titulo);  // Ahora puedes acceder directamente a los campos
        console.log("Texto de la noticia: ", noticia.value.texto);
    } else {
        console.log("No hay noticia seleccionada.");
    }
});

// Función para volver a la página anterior
const goBack = () => {
    router.push('/');
};
</script>