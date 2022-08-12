<script setup>
import {ref} from 'vue'

const menu_items = ref([])
</script>

<template>
  <li v-for="menu in menu_items"
      class="hover:bg-gray-100">
    <a
        :data-target="menu.name"
        @click="navigate"
        class="h-16 px-6 flex flex justify-center items-center w-full focus:text-orange-500">
      {{ menu.name }}
    </a>
  </li>
</template>
<script>
import axios from "axios";

export default {
  name: 'Menu',
  async created() {
    axios.get('http://localhost:8000/pet_types_api')
        .then(response => {
          this.menu_items = response.data
        })
        .catch(e => {
          console.log(e)
        })
  },
  methods: {
    navigate(event) {
      const clicked = event.target.getAttribute('data-target')
      this.$emit('clicked', clicked)

    }
  }
}
</script>
