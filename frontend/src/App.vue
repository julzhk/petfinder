<script setup>
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://vuejs.org/api/sfc-script-setup.html#script-setup
import Menu from "./components/Menu.vue";
import Logo from "./components/Logo.vue";
import {ref} from 'vue'
import Tile from "./components/Tile.vue";

const animal = ref('none')
const items = ref([])

</script>

<template>
  <div class="bg-gray-50 font-serif leading-normal tracking-normal">
    <div class="h-screen w-screen flex bg-gray-200">
      <!-- container -->
      <aside
          class="w-64 flex flex-col items-center bg-white text-gray-700 shadow h-full">
        <!-- Side Nav Bar-->
        <div class="h-16 flex items-center w-full">
          <!-- Logo Section -->
          <Logo/>
        </div>
        <ul>
          <!-- Items Section -->
          <Menu @clicked="handleClick"/>
        </ul>
      </aside>
      <div class="p-4">
        <div class="grid gap-4 grid-cols-3"
             id="animal-grid">

          <div class="contents"
               id="animal-grid-inner">
            <div v-for="animal in items">
              <Tile :animal="animal"/>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>

import axios from "axios";

export default {
  name: 'App',
  methods: {
    handleClick(event) {
      this.animal = event
      this.get_grid()
    },
    async get_grid() {
      axios.get('http://localhost:8000/grid_api?animal=' + this.animal)
          .then(response => {
            console.log(response)
            this.items = response.data
          })
          .catch(e => {
            console.log(e)
          })
    },
  }
}
</script>
