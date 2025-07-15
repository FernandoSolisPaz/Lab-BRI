<template>
  <v-app>
    <!-- Header -->
    <v-app-bar color="#e53e3e" dark height="60" flat width="230%">
      <v-toolbar-title class="text-h5 font-weight-bold d-flex align-center">
        <v-avatar size="40" class="mr-2" @click="$router.push('/')" style="cursor: pointer;">
          <v-img :src="logoUrl" alt="UrbanitApps Logo"></v-img>
        </v-avatar>
        DAILY SANTIAGO
      </v-toolbar-title>
    </v-app-bar>

    <!-- Main Content -->
    <v-main>
      <v-container fluid class="pa-0 ma-0">
        <RouterView /> <!-- Aquí se renderizará la vista activa, como NewsMap.vue -->
      </v-container>
    </v-main>
  </v-app>
</template>

<script setup>
import { ref } from 'vue';
import logoImage from './assets/urbanitappslogo.png';
const logoUrl = logoImage;
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
</style>