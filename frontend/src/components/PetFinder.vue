<script setup>
import {ref} from 'vue'

defineProps({
  msg: String
})

const count = ref(1)
const info = ref('no')

</script>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      posts: [],
      errors: []
    }
  },

  async created() {
    let config = {
      headers: {
        client_id:'XXX',
        client_secret:'YYY',
      }
    }
    axios.get('https://api.petfinder.com/v2/oauth2/token',config)
        .then(response => {
          // JSON responses are automatically parsed.
          this.info = response.data
          console.log(response)
        })
        .catch(e => {
          this.errors.push(e)
        })
  }
}
</script>


<template>
  <h1>{{ msg }}</h1>
  <div>
    <h5>Results: <small>{{ info.length }}</small></h5>
    <ul>
      <li v-for="result in info">
        {{ result.title }}
      </li>
    </ul>
  </div>
  <div class="bg-gray-200">
    <button class="rounded-full bg-blue-300" @click="count++">count is {{ count }}</button>
  </div>
</template>
