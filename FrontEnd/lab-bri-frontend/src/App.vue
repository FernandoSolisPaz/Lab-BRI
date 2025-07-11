<template>
  <v-app>
    <!-- Header -->
    <v-app-bar color="#e53e3e" dark height="60" flat width="230%">
      <v-toolbar-title class="text-h5 font-weight-bold">
        DAILY SANTIAGO
      </v-toolbar-title>
    </v-app-bar>

    <!-- Main Content -->
    <v-main>
      <v-container fluid class="pa-0 ma-0">
        <!-- Filter Section -->
        <v-card color="white" elevation="1" flat class="pa-4 w-100">
          <v-card-text class="pa-4">
            <v-row>
              <v-col cols="12" md="2">
                <v-menu
                  v-model="dateMenu"
                  :close-on-content-click="false"
                  transition="scale-transition"
                  offset-y
                  content-class="compact-datepicker-menu"
                >
                  <template v-slot:activator="{ props }">
                    <v-text-field
                      v-bind="props"
                      v-model="formattedDate"
                      label="Seleccionar fecha"
                      readonly
                      density="compact"
                      hide-details
                    >
                    <template #prepend-inner>
                      <i class="pi pi-calendar-clock"></i>
                    </template>
                  </v-text-field>
                  </template>
                  <v-date-picker 
                    v-model="selectedDate"
                    @update:model-value="dateMenu = false"
                    :show-adjacent-months="false"
                    hide-header
                  ></v-date-picker>
                </v-menu>
              </v-col>
              <v-col cols="12" md="2">
                <v-select
                  v-model="selectedComuna"
                  :items="comunaOptions"
                  label="Comuna"
                  variant="outlined"
                  density="compact"
                  placeholder="Buscar comuna"
                  hide-details
                ></v-select>
              </v-col>
              <v-col cols="12" md="2">
                <v-select
                  v-model="selectedCrimeType"
                  :items="crimeTypeOptions"
                  label="Tipo de delito"
                  variant="outlined"
                  density="compact"
                  placeholder="Seleccionar delito"
                  hide-details
                ></v-select>
              </v-col>
              <v-col cols="12" md="2">
                <v-select
                  v-model="selectedAgency"
                  :items="agencyOptions"
                  label="Agencia de noticias"
                  variant="outlined"
                  density="compact"
                  placeholder="Seleccionar agencia"
                  hide-details
                ></v-select>
              </v-col>
              <v-col cols="12" md="2">
                <v-select
                  v-model="selectedDocType"
                  :items="docTypeOptions"
                  label="Tipo de documento"
                  variant="outlined"
                  density="compact"
                  placeholder="Seleccionar tipo"
                  hide-details
                ></v-select>
              </v-col>
              <v-col cols="12" md="2">
                <v-select
                  v-model="selectedStatus"
                  :items="statusOptions"
                  label="Situación del caso"
                  variant="outlined"
                  density="compact"
                  placeholder="Seleccionar estado"
                  hide-details
                ></v-select>
              </v-col>
            </v-row>
            
            <!-- Search Bar -->
            <v-row class="mt-3">
              <v-col cols="12" md="4">
                <v-text-field
                  v-model="searchQuery"
                  placeholder="Buscar noticias..."
                  variant="outlined"
                  density="compact"
                  clearable
                  hide-details
                ><template #prepend-inner>
                      <i class="pi pi-search"></i>
                    </template></v-text-field>
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
        <RouterView />
      </v-container>
    </v-main>
  </v-app>

</template>

<script setup>
import { ref, watch, computed } from 'vue'
import 'primeicons/primeicons.css'

// Reactive variables
const selectedDate = ref(null)
const selectedComuna = ref(null)
const selectedCrimeType = ref(null)
const selectedAgency = ref(null)
const selectedDocType = ref(null)
const selectedStatus = ref(null)
const searchQuery = ref('')
const dateMenu = ref(false)

const comunaOptions = [
  'Estación Central',
  'Santiago',
  'Las Condes',
  'Providencia',
  'Ñuñoa',
  'Maipú'
]

const crimeTypeOptions = [
  'Homicidio',
  'Robo',
  'Hurto',
  'Violencia intrafamiliar',
  'Tráfico de drogas'
]

const agencyOptions = [
  'PDI',
  'Carabineros',
  'Fiscalía',
  'ECOH'
]

const docTypeOptions = [
  'Noticia',
  'Reportaje',
  'Entrevista',
  'Comunicado'
]

const statusOptions = [
  'En investigación',
  'Resuelto',
  'Archivado',
  'En proceso'
]

// Methods
const goBack = () => {
  // Para Nuxt, puedes usar:
  // await navigateTo('/') o $router.go(-1)
  console.log('Going back...')
}
const formattedDate = computed({
  get() {
    if (!selectedDate.value) return ''
    const date = new Date(selectedDate.value)
    const day = String(date.getDate()).padStart(2, '0')
    const month = String(date.getMonth() + 1).padStart(2, '0')
    const year = date.getFullYear()
    return `${day}/${month}/${year}`
  }
})
</script>

<style scoped>

.v-application {
  font-family: 'Roboto', sans-serif;
}

.text-blue {
  color: #1976d2;
  text-decoration: none;
}

.text-blue:hover {
  text-decoration: underline;
}
.v-card {
  background-color: white !important;
}

/* Mejorar la apariencia de los select */
.v-select .v-field {
  background-color: white;
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .d-flex.align-center {
    flex-direction: column;
    align-items: flex-start;
  }
  
  .text-h4 {
    margin-bottom: 1rem;
  }
  
  .v-chip.ml-4 {
    margin-left: 0 !important;
    align-self: flex-start;
  }
}
</style>

