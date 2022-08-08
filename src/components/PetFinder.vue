<script setup>
import {ref} from 'vue'

defineProps({
  msg: String
})

const count = ref(1)
</script>

<template>
  <h1>{{ msg }}</h1>
  <div class="bg-gray-200">
    <button class="rounded-full bg-blue-300" @click="count++">count is {{ count }}</button>
  </div>
</template>
