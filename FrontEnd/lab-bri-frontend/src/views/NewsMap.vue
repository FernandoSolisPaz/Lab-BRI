<template>
    <v-container fluid class="pa-0 ma-0 fill-height">
        <v-row no-gutters class="fill-height">

            <!-- Filtros: Columna con filtros (por encima de todo) -->
            <v-col cols="12" class="pa-2">
                <v-card color="white" elevation="1" flat class="pa-4 w-100">
                    <v-card-text class="pa-4">
                        <v-row>
                            <v-col cols="12" md="2">
                                <v-menu v-model="dateMenu" :close-on-content-click="false" transition="scale-transition"
                                    offset-y content-class="compact-datepicker-menu">
                                    <template v-slot:activator="{ props }">
                                        <v-text-field v-bind="props" v-model="formattedDate" label="Seleccionar fecha"
                                            readonly density="compact" hide-details @update:modelValue="onInputChange">
                                            <template #prepend-inner>
                                                <i class="pi pi-calendar-clock"></i>
                                            </template>
                                        </v-text-field>
                                    </template>
                                    <v-date-picker v-model="selectedDate" @update:model-value="dateMenu = false"
                                        :show-adjacent-months="false" hide-header
                                        @update:modelValue="onInputChange"></v-date-picker>
                                </v-menu>
                            </v-col>
                            <v-col cols="12" md="2">
                                <v-select v-model="selectedComuna" :items="['Selecciona...', ...comunaOptions]"
                                    label="Comuna" variant="outlined" density="compact" placeholder="Buscar comuna"
                                    hide-details @update:modelValue="onInputChange"></v-select>
                            </v-col>
                            <v-col cols="12" md="2">
                                <v-select v-model="selectedCrimeType" :items="['Selecciona...', ...crimeTypeOptions]"
                                    label="Tipo de delito" variant="outlined" density="compact"
                                    placeholder="Seleccionar delito" hide-details
                                    @update:modelValue="onInputChange"></v-select>
                            </v-col>
                            <v-col cols="12" md="2">
                                <v-select v-model="selectedAgency" :items="['Selecciona...', ...agencyOptions]"
                                    label="Fuente de noticias" variant="outlined" density="compact"
                                    placeholder="Seleccionar fuente" hide-details
                                    @update:modelValue="onInputChange"></v-select>
                            </v-col>
                            <v-col cols="12" md="2">
                                <v-select v-model="selectedDocType" :items="['Selecciona...', ...docTypeOptions]"
                                    label="Tipo de documento" variant="outlined" density="compact"
                                    placeholder="Seleccionar tipo" hide-details
                                    @update:modelValue="onInputChange"></v-select>
                            </v-col>
                            <v-col cols="12" md="2">
                                <v-select v-model="selectedStatus" :items="['Selecciona...', ...statusOptions]"
                                    label="Situación del caso" variant="outlined" density="compact"
                                    placeholder="Seleccionar estado" hide-details
                                    @update:modelValue="onInputChange"></v-select>
                            </v-col>
                        </v-row>

                        <!-- Barra de búsqueda -->
                        <v-row class="mt-3">
                            <v-col cols="12" md="4">
                                <v-text-field v-model="searchQuery" placeholder="Buscar noticias..." variant="outlined"
                                    density="compact" clearable hide-details @update:modelValue="onInputChange">
                                    <template #prepend-inner>
                                        <i class="pi pi-search"></i>
                                    </template>
                                </v-text-field>
                            </v-col>
                        </v-row>
                    </v-card-text>
                </v-card>
            </v-col>


            <!-- Columna izquierda: Lista de noticias -->
            <v-col cols="12" md="3" class="pa-2 fill-height">
                <v-card class="d-flex flex-column" height="100%">
                    <v-card-title class="text-h6 font-weight-bold">
                        Noticias
                    </v-card-title>
                    <v-divider></v-divider>

                    <!-- Scroll solo aquí -->
                    <v-card-text class="scrollable-news">
                        <!-- Verifica si hay noticias -->
                        <div v-if="noticias.length === 0">
                            <p>No hay noticias</p> <!-- Muestra este mensaje si la lista de noticias está vacía -->
                        </div>

                        <!-- Si hay noticias, muestra la lista -->
                        <div v-else>
                            <div v-for="(noticia, index) in noticias" :key="index" class="mb-4 d-flex">
                                <!-- Logo -->
                                <v-img :src="getLogo(noticia.document.pagina)" width="60" height="60"
                                    class="mr-3 rounded" cover />
                                <!-- Contenido -->
                                <div class="flex-grow-1">
                                    <div class="text-subtitle-1 font-weight-bold mb-1">
                                        {{ noticia.document.titulo.slice(0, 55) }}...
                                    </div>
                                    <div class="text-body-2">
                                        {{ noticia.document.texto.slice(0, 200) }}...
                                    </div>
                                    <div class="d-flex justify-end my-3">
                                        <v-btn color="red" variant="elevated" size="small" :href="noticia.hipervinculo">
                                            Ver más
                                        </v-btn>
                                    </div>
                                    <v-divider></v-divider>
                                </div>
                            </div>
                        </div>
                    </v-card-text>
                </v-card>
            </v-col>

            <!-- Columna derecha: MAPA -->
            <v-col cols="12" md="9" class="pa-1 fill-height">
                <Map ref="map" />
            </v-col>

        </v-row>

    </v-container>
</template>

<script>
import Map from '../components/Map.vue'
import appService from '@/services/app.service'

export default {
    components: {
        Map
    },

    data() {
        return {
            noticias: [

            ],

            poligonos: [],
            dateMenu: false,
            selectedDate: null,
            selectedComuna: null,
            selectedCrimeType: null,
            selectedAgency: null,
            selectedDocType: null,
            selectedStatus: null,
            searchQuery: '',
            comunaOptions: ['Estación Central', 'Santiago', 'Las Condes', 'Providencia', 'Ñuñoa', 'Maipú', 'Quilicura'],
            crimeTypeOptions: ['Homicidio', 'Robo', 'Hurto', 'Violencia intrafamiliar', 'Tráfico de drogas', 'Fallecido'],
            agencyOptions: ['PDI', 'Carabineros', 'Fiscalía', 'ECOH', 'T13'],
            docTypeOptions: ['Noticia', 'Reportaje', 'Entrevista', 'Comunicado'],
            statusOptions: ['En investigación', 'Resuelto', 'Archivado', 'En proceso'],
        }
    },

    methods: {
        getLogo(pagina) {
            const logos = {
                "BioBio Chile": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRxaKtXVa_5rXYa3Jv-L65j6h9xNofU4oeTkw&s",
                "CNN Chile": "https://upload.wikimedia.org/wikipedia/commons/0/04/Logo_cnnchile.png",
                "La Tercera": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzn9W65Z27kiAcLB-2YZysqTSS_EDoqvCtng&s",
                "CHV Noticias": "https://upload.wikimedia.org/wikipedia/commons/e/ef/Logo_CHV_2015.png",
                "Mega Noticias": "https://static-cdn.jtvnw.net/jtv_user_pictures/6c5d6466-2ab2-4bf7-9e4d-79b156e08823-profile_image-300x300.png",
                "Radio Cooperativa": "https://app.cooperativa.cl/apps/site/artic/20220718/imag/foto_0000001220220718133642.png",
                "T13": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Logotipo_de_Teletrece.svg/1200px-Logotipo_de_Teletrece.svg.png",
            }
            return logos[pagina] || "https://i.pinimg.com/1200x/7b/71/35/7b7135945421f5d2a7e3b11830f8f227.jpg"
        },

        async obtenerPoligonos() {
            // Se obtienen las comunas
            appService.listarComunas()
                .then(response => {
                    this.poligonos = response.data; // Asignamos los datos de la respuesta
                    console.log('Se obtuvieron los poligonos', response.data); // Manejamos errores

                    // Una vez que los polígonos estén cargados, seleccionamos una comuna aleatoria
                    this.seleccionarComunaAleatoria(); // Llama la función para seleccionar la comuna

                    // Lista de colores predefinidos
                    const colores = [
                        '#8a2be2', '#7fff00', '#ff6347', '#ff4500', '#ff1493',
                        '#00bfff', '#4682b4', '#2e8b57', '#ffd700', '#dc143c',
                        '#ff8c00', '#9932cc', '#8b0000', '#3cb371', '#8fbc8f',
                        '#20b2aa', '#d2691e', '#00fa9a', '#f08080', '#e9967a',
                        '#dda0dd', '#b0c4de', '#ff69b4', '#a52a2a', '#ff00ff',
                        '#ffdead', '#f5deb3', '#ffb6c1', '#c71585', '#add8e6',
                        '#b22222', '#5f9ea0', '#f0e68c'
                    ];

                    // // Llamamos a la función solo después de que los datos estén cargados
                    // if (this.poligonos) {
                    //     this.poligonos.forEach((comuna, index) => {
                    //         const coords = comuna.geometria.coordinates[0];
                    //         const color = colores[index % colores.length]; // Asegura que si hay más de 33 se repitan colores
                    //         this.dibujarPoligono(coords, color);
                    //     });
                    // }
                })
                .catch(error => {
                    console.error('Error al obtener los poligonos:', error); // Manejamos errores
                });
        },

        dibujarPoligono(poligon, color = "purple", clearPrevious = true) {
            const coords = poligon;

            // Usamos el color pasado como argumento
            const opciones = {
                color: color,        // Borde del polígono
                fillColor: color,    // Color de relleno del polígono
                fillOpacity: 0.4,    // Opacidad del relleno
            };

            // Accede al método de Map.vue a través del ref
            this.$refs.map.putPolygon(coords, opciones, true, true, clearPrevious);
        },

        onInputChange() {
            console.log("Se ha realizado un cambio en los filtrossssssssssssssss.");
            const query = {
                texto: this.searchQuery || "",
                pagina: this.selectedAgency === "Selecciona..." ? "" : this.selectedAgency || "",
                ubicacion: this.selectedComuna === "Selecciona..." ? "" : this.selectedComuna || "",
                keywords: [this.selectedCrimeType === "Selecciona..." ? "" : this.selectedCrimeType || ""],
                autores: [""],
                exact_date: "",
                after_date: "",
                before_date: "",
            };

            console.log("ESTA ES LA QUERY: ", query);

            appService.buscarDocumento(query)
                .then(response => {
                    this.noticias = response.data.hits; // Asignamos los datos de la respuesta
                    console.log("ESTAS SON LAS NOTICIAS: ", this.noticias);
                })
                .catch(error => {
                    console.error('Error al obtener las noticias:', error); // Manejamos errores
                });

            if (this.selectedComuna) {
                const comuna = this.poligonos.find(p => p.nombre === this.selectedComuna);
                if (comuna) {
                    this.dibujarPoligono(comuna.geometria.coordinates[0], "purple"); // Dibuja el polígono con color morado
                }
            }
        },

        // Función para seleccionar una comuna aleatoria al cargar la página
        seleccionarComunaAleatoria() {
            const randomIndex = Math.floor(Math.random() * this.comunaOptions.length);
            this.selectedComuna = this.comunaOptions[randomIndex]; // Selecciona aleatoriamente una comuna
            this.onInputChange(); // Llama a la función de cambio para que se ejecute la lógica
        }
    },

    mounted() {
        this.obtenerPoligonos();

    },

    computed: {
        formattedDate() {
            if (!this.selectedDate) return '';
            const date = new Date(this.selectedDate);
            const day = String(date.getDate()).padStart(2, '0');
            const month = String(date.getMonth() + 1).padStart(2, '0');
            const year = date.getFullYear();
            return `${day}/${month}/${year}`;
        }
    }
}
</script>

<style scoped>
.fill-height {
    height: 100vh;
}

.scrollable-news {
    overflow-y: auto;
    flex-grow: 1;
    max-height: 73vh;
    /* Ajusta si tu app-bar mide distinto */
}

.truncate {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}

.truncate-multiline {
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
}

.scrollable-news::-webkit-scrollbar {
    width: 20px;
}

.scrollable-news::-webkit-scrollbar-track {
    background: #f0ccc4;
    /* Fondo del scrollbar */
    border-radius: 4px;
}

.scrollable-news::-webkit-scrollbar-thumb {
    background-color: #e53e3e;
    /* Rojo brillante */
    border-radius: 6px;
    border: 2px solid transparent;
    /* Para espacio alrededor del thumb */
    background-clip: content-box;
}

.scrollable-news::-webkit-scrollbar-thumb:hover {
    background-color: #c53030;
    /* Rojo oscuro al pasar el mouse */
}
</style>
