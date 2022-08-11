<script setup>
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://vuejs.org/api/sfc-script-setup.html#script-setup
import PetFinder from "./components/PetFinder.vue";
import MenuItem from "./MenuItem.vue";
import Logo from "./Logo.vue";</script>

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
          <MenuItem/>
        </ul>
      </aside>
      <div class="p-4">
        <div class="grid gap-4 grid-cols-3"
             id="animal-grid">
          <PetFinder />
        </div>
      </div>
    </div>
  </div>
</template>
