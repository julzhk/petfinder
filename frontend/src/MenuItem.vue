<template>
  <li class="hover:bg-gray-100">
    <a hx-post="{% url 'gallery' %}?type=NAME|urlencode }}"
       hx-target="#animal-grid"
       class="h-16 px-6 flex flex justify-center items-center w-full focus:text-orange-500">
      animal_type.name
    </a>
  </li>
</template>
<script>
export default {
  name: 'MenuItem'
}
</script>