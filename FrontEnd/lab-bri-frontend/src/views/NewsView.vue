<template>
    <main class="news-view">
        <v-container>
                <!-- Article Content -->
                <v-card flat color="white" elevation="4">
                    <v-card-text class="pa-6">
                    <!-- Back Button and Title -->
                    <div class="d-flex align-center mb-4">
                        <v-btn
                        icon
                        variant="text"
                        size="small"
                        class="mr-3"
                        @click="goBack"
                        >
                        <v-icon>mdi-arrow-left</v-icon>
                        </v-btn>
                        
                        <h1 class="text-h4 font-weight-bold flex-grow-1">
                        Balacera en fiesta clandestina en Estación Central deja un muerto y al menos tres heridos
                        </h1>
                        <v-img :src="getLogo('T13')" width="60" height="60" class="mr-3 rounded" cover />
                        <a href="https://www.t13.cl/noticia/nacional/balacera-fiesta-clandestina-estacion-central-deja-muerto-al-menos-tres-heridos-7-6-2025" class="text-blue" target="_blank">Link de la noticia</a>

                    </div>

                    <!-- Article Content -->
                    <div class="mb-6">
                        <p class="text-body-1 mb-4">
                        El Equipo ECOH de la Fiscalía Metropolitana y la Brigada de Homicidios de la PDI están investigando un violento 
                        <a href="#" class="text-blue">homicidio</a> ocurrido durante la madrugada de esta sábado en la calle Arica, comuna de Estación Central, Región Metropolitana.
                        </p>
                        
                        <p class="text-body-1 mb-6">
                        Un hombre fue asesinado con arma de fuego y al menos otras tres personas resultaron heridas durante una balacera registrada al interior de una fiesta de carácter clandestino.
                        </p>
                    </div>

                    <!-- Article Image -->
                    <div class="mb-4">
                        <v-img
                        src="https://s.t13.cl/sites/default/files/styles/manualcrop_1600x800/public/t13/field-imagen/2025-06/Gs1TSRnXQAAIhIC.jpg.jpeg?itok=GkJRzWk4"
                        alt="Balacera en fiesta clandestina en Estación Central"
                        class="rounded"
                        cover
                        max-height="400"
                        >
                        <template v-slot:placeholder>
                            <div class="d-flex align-center justify-center fill-height">
                            <v-progress-circular
                                color="grey-lighten-4"
                                indeterminate
                            ></v-progress-circular>
                            </div>
                        </template>
                        </v-img>
                        <p class="text-caption text-grey-darken-1 mt-2">
                        Balacera en fiesta clandestina en Estación Central deja un muerto y al menos tres heridos - X ECOH
                        </p>
                    </div>

                    <!-- Additional Article Content -->
                    <div class="mb-4">
                        <p class="text-body-1">
                        Según información preliminar entregada por el fiscal ECOH Francisco Morales, 
                        tres heridos llegaron por sus propios medios al 
                        <a href="#" class="text-blue">Hospital San Juan de Dios</a>, 
                        todos de nacionalidad extranjera. A raíz de este ingreso, Carabineros se 
                        trasladó al lugar de los hechos, donde fue hallado el cuerpo sin vida de un 
                        hombre que habría recibido un disparo en la zona de la cadera.
                        </p>
                    </div>

                    <!-- Source Badge -->
                    <v-chip
                        color="orange"
                        text-color="white"
                        size="small"
                        class="mt-2"
                    >
                        Fuente noticia
                    </v-chip>
        </v-card-text>
        </v-card>
        </v-container>
    </main>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'
import{ getLogo } from '../utils/logos'

const router = useRouter()

const goBack = async () => {
  await router.push('/')
  console.log('Going back...')
}

</script>