<template>
    <v-container fluid class="pa-0 ma-0 fill-height">
        <v-row no-gutters class="fill-height">

            <!-- Filtros: Columna con filtros (por encima de todo) -->
            <v-col cols="12" class="pa-2">
                <v-card color="white" elevation="1" flat class="pa-4 w-100">
                    <v-card-text class="pa-4">
                        <v-row>
                            <v-col cols="12" md="3">
                                <div class="d-flex align-center">
                                    <v-menu class="flex-grow-1" v-model="dateMenuStart" :close-on-content-click="false"
                                        transition="scale-transition" offset-y content-class="compact-datepicker-menu">
                                        <template #activator="{ props }"> <v-text-field v-bind="props"
                                                v-model="formattedStartDate" label="Seleccionar fecha inicial" readonly
                                                density="compact" hide-details @update:modelValue="onInputChange">
                                                <template #prepend-inner>
                                                    <i class="pi pi-calendar-clock" />
                                                </template>
                                            </v-text-field>
                                        </template>
                                        <v-date-picker v-model="selectedStartDate"
                                            @update:model-value="dateMenuStart = false" :show-adjacent-months="false"
                                            hide-header @update:modelValue="onInputChange" />
                                    </v-menu>
                                    <v-tooltip bottom>
                                        <template #activator="{ props, on }">
                                            <v-icon v-bind="props" v-on="on" class="ml-2" small>
                                                mdi-help-circle-outline
                                            </v-icon>
                                        </template>
                                        <span>
                                            En caso de seleccionar únicamente fecha inicial, se tomará como fecha exacta
                                            de búsqueda
                                        </span>
                                    </v-tooltip>
                                </div>
                            </v-col>
                            <v-col cols="12" md="2">
                                <v-menu v-model="dateMenuEnd" :close-on-content-click="false"
                                    transition="scale-transition" offset-y content-class="compact-datepicker-menu">
                                    <template v-slot:activator="{ props }">
                                        <v-text-field v-bind="props" v-model="formattedEndDate"
                                            label="Seleccionar fecha final" :disabled="!selectedStartDate" readonly
                                            density="compact" hide-details @update:modelValue="onInputChange">
                                            <template #prepend-inner>
                                                <i class="pi pi-calendar-clock"></i>
                                            </template>
                                        </v-text-field>
                                    </template>
                                    <v-date-picker v-model="selectedEndDate" @update:model-value="dateMenuEnd = false"
                                        :show-adjacent-months="false" hide-header
                                        @update:modelValue="onInputChange"></v-date-picker>
                                </v-menu>
                            </v-col>
                            <v-col cols="12" md="2">
                                <v-select v-model="selectedComuna" :items="['Selecciona...', ...comunaOptions]"
                                    label="Comuna" variant="outlined" density="compact" placeholder="Buscar comuna"
                                    hide-details @update:modelValue="onMapClick"></v-select>
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
                        </v-row>

                        <!-- Barra de búsqueda -->
                        <v-row class="mt-3">
                            <v-col cols="12" md="4">
                                <v-text-field v-model="searchQuery" placeholder="Buscar noticias..." variant="outlined"
                                    density="compact" clearable hide-details @update:modelValue="onInputChange"
                                    :style="{ borderColor: 'black' }">
                                    <template #prepend-inner>
                                        <i class="pi pi-search"></i>
                                    </template>
                                    <template #append-inner>
                                        <i class="pi pi-search"></i>
                                    </template>
                                </v-text-field>
                            </v-col>

                            <v-col cols="12" md="8" class="d-flex justify-end align-center">
                    
                                <v-switch v-model="heatmapMode" :color="heatmapMode ? 'red' : undefined"
                                    label="Activar modo mapa de calor" @update:modelValue="toggleHeatmapMode"
                                    hide-details inset />
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
                                        <v-btn color="red" variant="elevated" size="small" @click="verMas(noticia)">
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
                <Map ref="map" @poligono-click="onMapClick" />
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
            noticiaSeleccionada: null,

            poligonos: [],
            dateMenuStart: false,
            dateMenuEnd: false,
            selectedStartDate: null,
            selectedEndDate: null,
            selectedComuna: null,
            selectedCrimeType: null,
            selectedAgency: null,
            selectedDocType: null,
            selectedStatus: null,
            searchQuery: '',
            comunaOptions: ['Cerrillos', 'Cerro Navia', 'Conchalí', 'El Bosque', 'Estación Central', 'Huechuraba', 'Independencia', 'La Cisterna', 'La Florida', 'La Granja', 'La Pintana', 'La Reina', 'Las Condes', 'Lo Barnechea', 'Lo Espejo', 'Lo Prado', 'Macul', 'Maipú', 'Ñuñoa', 'Pedro Aguirre Cerda', 'Peñalolén', 'Providencia', 'Pudahuel', 'Quilicura', 'Quinta Normal', 'Recoleta', 'Renca', 'San Joaquín', 'San Miguel', 'San Ramón', 'Santiago', 'Vitacura'],
            crimeTypeOptions: ['Homicidio', 'Robo', 'Hurto', 'Violencia intrafamiliar', 'Tráfico de drogas', 'Asesinato'],
            agencyOptions: ['ECOH', 'Radio Duna', 'El Dinamo', 'Emol', 'Radio ADN', 'BioBio Chile', 'CNN Chile', 'La Tercera', 'CHV Noticias', 'Mega Noticias', 'Radio Cooperativa', 'T13'],
            formattedStartDate: '',
            formattedEndDate: '',
            heatmapMode: false,
        }
    },

    methods: {
        getLogo(pagina) {
            const logos = {
                "PDI": "https://upload.wikimedia.org/wikipedia/commons/9/97/Polic%C3%ADa_de_Investigaciones_de_Chile_%28PDI%29_01.jpg",
                "Carabineros": "https://images.steamusercontent.com/ugc/2126318308534247985/D2B95F860D2D88AD6AC0A2C201CE4C25D61BCA73/?imw=637&imh=358&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=true",
                "Fiscalía": "https://pbs.twimg.com/profile_images/1807767458452803584/mVWy65iB_400x400.jpg",
                "ECOH": "https://santacruzfm.cl/wp-content/uploads/elementor/thumbs/WhatsApp-Image-2023-11-14-at-16.42.07-qq3ithcoq1l2lft14p0p7dr87v7qdqicxqgfngosyu.jpeg",
                "Radio Duna": "https://cdn-profiles.tunein.com/s25108/images/logog.jpg?t=155673",
                "El Dinamo": "https://www.eldinamo.cl/_templates/globals/img/logo.jpg",
                "Emol": "https://pbs.twimg.com/profile_images/816281345747980288/XtL97I6M_400x400.jpg",
                "Radio ADN": "https://p16-common-sign-va.tiktokcdn-us.com/tos-maliva-avt-0068/5da1a2716098c787c0f3878f26c461d0~tplv-tiktokx-cropcenter:720:720.jpeg?dr=9640&refresh_token=205c0e40&x-expires=1752746400&x-signature=3VJHJPvvOOjcvt8Y2DnfA0XNsOc%3D&t=4d5b0474&ps=13740610&shp=a5d48078&shcp=81f88b70&idc=useast8",
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

        verMas(noticia) {
            this.noticiaSeleccionada = noticia;
            console.log("Noticia seleccionada: ", this.noticiaSeleccionada.document.titulo);

            localStorage.setItem('noticiaSeleccionada', JSON.stringify(noticia.document));

            this.$router.push({ name: 'newsview' });
        },

        onMapClick(comunaNombre) {
            this.selectedComuna = comunaNombre;
            console.log("onMapClick", this.selectedComuna)
            this.onInputChange();
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
                        '#8a2be2'
                    ];

                    // Llamamos a la función solo después de que los datos estén cargados
                    if (this.poligonos) {
                        this.poligonos.forEach((comuna, index) => {
                            const coords = comuna.geometria.coordinates[0];
                            const color = colores[index % colores.length]; // Asegura que si hay más de 33 se repitan colores
                            this.dibujarPoligono(coords, color, /* clearPrevious */ false, comuna.nombre);
                        });
                    }
                })
                .catch(error => {
                    console.error('Error al obtener los poligonos:', error); // Manejamos errores
                });
        },

        dibujarPoligono(poligon, color = "purple", clearPrevious = true, comunaNombre = null) {
            const coords = poligon;

            // Usamos el color pasado como argumento
            const opciones = {
                color: color,        // Borde del polígono
                fillColor: color,    // Color de relleno del polígono
                fillOpacity: 0.5,    // Opacidad del relleno
            };

            // Accede al método de Map.vue a través del ref
            this.$refs.map.putPolygon(coords, opciones, true, true, clearPrevious, comunaNombre);
        },

        dibujarTodasBase() {
            const colorBase = '#8a2be2';
            this.poligonos.forEach((comuna, i) => {
                const coords = comuna.geometria.coordinates[0];
                this.dibujarPoligono(coords, colorBase, i === 0, comuna.nombre);
            });
        },

        resaltarSeleccionada(newVal, oldVal) {
            if (this.heatmapMode) return;
            if (!newVal || newVal === "Selecciona...") return;

            const sel = this.poligonos.find(p => p.nombre === newVal);
            const prevcomuna = this.poligonos.find(p => p.nombre === oldVal);

            if (!sel) return;

            if (oldVal && oldVal !== "Selecciona..." && prevcomuna) {
                this.$refs.map.removePolygonByComuna(oldVal);
            }

            this.dibujarPoligono(sel.geometria.coordinates[0], 'purple', false, sel.nombre);
        },

        onInputChange() {
            console.log("Se ha realizado un cambio en los filtros.");
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

            // Si solo hay fecha "Desde" seleccionada → exact_date
            if (this.selectedStartDate && !this.selectedEndDate) {
                query.exact_date = this.selectedStartDate;
            }
            // Si hay rango completo → after_date = Desde, before_date = Hasta
            else if (this.selectedStartDate && this.selectedEndDate) {
                query.after_date = this.selectedStartDate;
                query.before_date = this.selectedEndDate;
            }

            console.log("ESTA ES LA QUERY: ", query);

            appService.buscarDocumento(query)
                .then(response => {
                    this.noticias = response.data.hits; // Asignamos los datos de la respuesta
                    console.log("ESTAS SON LAS NOTICIAS: ", this.noticias);
                })
                .catch(error => {
                    console.error('Error al obtener las noticias:', error); // Manejamos errores
                });
        },

        // Función para seleccionar una comuna aleatoria al cargar la página
        seleccionarComunaAleatoria() {
            const randomIndex = Math.floor(Math.random() * this.comunaOptions.length);
            this.selectedComuna = this.comunaOptions[randomIndex]; // Selecciona aleatoriamente una comuna
            this.onInputChange(); // Llama a la función de cambio para que se ejecute la lógica
        },

        getHeatmapColor(value) {
            const r = 255;
            // Verde va de 255 → 165 → 0 dependiendo del valor
            let g;
            if (value < 0.5) {
                g = 255 - value * 2 * (255 - 165); // Amarillo a Naranjo
            } else {
                g = 165 - (value - 0.5) * 2 * 165; // Naranjo a Rojo
            }
            g = Math.max(0, Math.floor(g)); // Asegura que no sea negativo
            return `rgb(${r},${g},0)`;
        },

        async toggleHeatmapMode(isActive) {
            if (!isActive) {
                this.dibujarTodasBase(); // Vuelve a colorear los polígonos base
                this.resaltarSeleccionada(this.selectedComuna, null);
                return;
            }

            try {
                const response = await appService.buscarDocumento({
                    texto: "", pagina: "", ubicacion: "", keywords: [""]
                });

                const noticias = response.data.hits;

                const conteoPorComuna = {};
                noticias.forEach(n => {
                    const comuna = n.document.ubicacion;
                    if (comuna) conteoPorComuna[comuna] = (conteoPorComuna[comuna] || 0) + 1;
                });

                const valores = Object.values(conteoPorComuna);
                const max = Math.max(...valores);
                const min = Math.min(...valores);

                this.$refs.map.clearMarkers();

                this.poligonos.forEach(p => {
                    const cantidad = conteoPorComuna[p.nombre] || 0;
                    const normalized = max === min ? 0 : (cantidad - min) / (max - min);
                    const color = this.getHeatmapColor(normalized);
                    this.dibujarPoligono(p.geometria.coordinates[0], color, false, p.nombre);
                });

            } catch (error) {
                console.error("Error al cargar datos de mapa de calor", error);
            }
        },
    },

    watch: {
        selectedComuna(newVal, oldVal) {
            // Si está activado el mapa de calor, no hacer nada
            if (this.heatmapMode) return;

            // Si se selecciona "Selecciona...", eliminar el anterior si existe
            if (newVal === "Selecciona...") {
                if (oldVal && oldVal !== "Selecciona...") {
                    this.$refs.map.removePolygonByComuna(oldVal);
                }
                return;
            }

            // Si se selecciona una comuna válida
            this.resaltarSeleccionada(newVal, oldVal);
        }
    },

    mounted() {
        this.obtenerPoligonos();
        this.dibujarTodasBase();

    },

    computed: {
        formattedStartDate() {
            if (!this.selectedStartDate) return ''
            const d = new Date(this.selectedStartDate)
            return `${String(d.getDate()).padStart(2, '0')}/${String(d.getMonth() + 1).padStart(2, '0')}/${d.getFullYear()}`
        },
        formattedEndDate() {
            if (!this.selectedEndDate) return ''
            const d = new Date(this.selectedEndDate)
            return `${String(d.getDate()).padStart(2, '0')}/${String(d.getMonth() + 1).padStart(2, '0')}/${d.getFullYear()}`
        }
    },
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
