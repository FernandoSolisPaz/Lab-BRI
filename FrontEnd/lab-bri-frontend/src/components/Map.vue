<template>
  <div id="map" class="map-container"></div>
</template>

<script>
import L from "leaflet";
import "leaflet/dist/leaflet.css";
import greypng from "../assets/marker-icon-2x-grey.png";
import redpng from "../assets/marker-icon-2x-red.png";
import storeicon from "../assets/store5.png";
import clienticon from "../assets/client.png";
import ordericon from "../assets/order2.png";
import deliveryicon from "../assets/shipment.png";
import { polygon } from "leaflet";

export default {
  name: "Map",
  data() {
    return {
      map: null, // Almacena la instancia del mapa Leaflet
      circleGroup: null, // Almacena el grupo de círculos
      markerGroup: null, // Almacena el grupo de marcadores
      polygonGroup: null
    };
  },
  mounted() {
    // Inicializa el mapa cuando el componente está montado
    this.map = L.map("map").setView([-33.45121494496883, -70.68451593558727], 7);

    // Agrega la capa base de OpenStreetMap
    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
      attribution:
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    }).addTo(this.map);

    // Inicializa los grupos de capas para marcadores y círculos
    this.circleGroup = L.layerGroup().addTo(this.map);
    this.markerGroup = L.layerGroup().addTo(this.map);
    this.polygonGroup = L.layerGroup().addTo(this.map); // Asegúrate de inicializar polygonGroup
  },
  methods: {
    // Agrega un marcador al mapa
    putMarker(name, lat, lon, icon = null) {
      let marker;
      switch (icon) {
        case "store":
          const storeIcon = new L.Icon({
            iconUrl: storeicon,
            shadowUrl:
              "https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png",
            iconSize: [60, 60],
            iconAnchor: [12, 41],
            popupAnchor: [1, -34],
            shadowSize: [41, 41],
          });
          marker = L.marker([lat, lon], { title: name, icon: storeIcon });
          break;
        case "order":
          const orderIcon = new L.Icon({
            iconUrl: ordericon,
            shadowUrl:
              "https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png",
            iconSize: [50, 50],
            iconAnchor: [12, 41],
            popupAnchor: [1, -34],
            shadowSize: [41, 41],
          });
          marker = L.marker([lat, lon], { title: name, icon: orderIcon });
          break;
        case "delivery":
          const deliveryIcon = new L.Icon({
            iconUrl: deliveryicon,
            shadowUrl:
              "https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png",
            iconSize: [50, 50],
            iconAnchor: [12, 41],
            popupAnchor: [1, -34],
            shadowSize: [41, 41],
          });
          marker = L.marker([lat, lon], { title: name, icon: deliveryIcon });
          break;
        case "client":
          const clientIcon = new L.Icon({
            iconUrl: clienticon,
            shadowUrl:
              "https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png",
            iconSize: [50, 50],
            iconAnchor: [12, 41],
            popupAnchor: [1, -34],
            shadowSize: [41, 41],
          });
          marker = L.marker([lat, lon], { title: name, icon: clientIcon });
          break;
        default:
          marker = L.marker([lat, lon], { title: name });
      }
      this.markerGroup.addLayer(marker); // Agrega el marcador al grupo
    },

    // Limpia todos los marcadores del mapa
    clearMarkers() {
      this.markerGroup.clearLayers();
      this.circleGroup.clearLayers();
      this.polygonGroup.clearLayers();
    },

    // Dibuja un círculo en el mapa
    putCircle(lat, lon, rad) {
      this.circleGroup.clearLayers(); // Limpia cualquier círculo existente
      const circle = L.circle([lat, lon], { radius: rad }); // Crea un nuevo círculo
      this.circleGroup.addLayer(circle); // Agrega el círculo al grupo
    },

    removePolygonByComuna(comunaNombre) {

      let leafletId = null;

      this.polygonGroup.eachLayer(layer => {
        if (layer._comunaNombre === comunaNombre) {
          console.log(layer._comunaNombre)
          leafletId = layer._leaflet_id;
        }
      });
      console.log('Este es el idLEAF de la comuna a eliminar:', leafletId)
      this.polygonGroup.removeLayer(leafletId);
    },

    putPolygon(polygon, options = {}, invert = false, zoomToFit = true, clearPrevious = true, comunaNombre = null, heatmapMode = false) {
      // Solo limpia los polígonos previos si clearPrevious es verdadero
      if (clearPrevious) {
        this.polygonGroup.clearLayers();
      }

      const defaultOptions = {
        color: "red",
        fillColor: "lightpink",
        fillOpacity: 0.5,
        weight: 2,
      };
      const mergedOptions = { ...defaultOptions, ...options };

      const coords = invert
        ? polygon.map(coord => [coord[1], coord[0]])  // Invertir si es necesario
        : polygon;

      const leafletPolygon = L.polygon(coords, mergedOptions);
      leafletPolygon._comunaNombre = comunaNombre;

        if (comunaNombre && !heatmapMode) {
          leafletPolygon.on('click', () => {
            this.$emit('poligono-click', comunaNombre);
          });
        }

      this.polygonGroup.addLayer(leafletPolygon);

      // Centrar y hacer zoom al polígono
      if (zoomToFit && this.map) {
        this.map.fitBounds(leafletPolygon.getBounds(), {
          padding: [20, 20] // opcional: agrega espacio visual alrededor
        });
      }
    },
  },
};
</script>

<style scoped>
.map-container {
  width: 100%;
  height: 78vh;
}
</style>