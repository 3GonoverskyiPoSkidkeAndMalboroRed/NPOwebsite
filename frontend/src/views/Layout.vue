<template>
  <div class="min-h-screen bg-background">
    <Navbar />
    <main class="pt-16">
      <router-view />
    </main>
  </div>
</template>

<script setup lang="ts">
import Navbar from "@/components/Navbar.vue";
</script>
