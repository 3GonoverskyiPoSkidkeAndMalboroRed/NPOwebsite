<template>
  <div class="min-h-screen bg-background">
    <!-- Hero Section -->
    <section class="py-20 px-4 bg-gradient-to-b from-background to-muted/20">
      <div class="max-w-7xl mx-auto">
        <div class="text-center mb-16">
          <h1 class="text-4xl md:text-6xl font-bold mb-6 bg-gradient-to-r from-primary to-primary/70 bg-clip-text">
            Решаемые задачи
          </h1>

        </div>

        <!-- Основные категории задач -->
        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8 mb-16">
          <a href="/methods-expert" class="block relative rounded-lg p-6 border hover:shadow-lg transition-shadow overflow-hidden cursor-pointer" style="background-image: url('/home-photo/expertlittle.png'); background-size: cover; background-position: center;">
            <div class="absolute inset-0 bg-black/40 hover:bg-black/30 transition-colors"></div>
            <div class="relative z-10">
              <h3 class="text-xl font-semibold text-white">Оборудование для экспертизы</h3>
            </div>
          </a>

          <a href="/methods-oil" class="block relative rounded-lg p-6 border hover:shadow-lg transition-shadow overflow-hidden cursor-pointer" style="background-image: url('/home-photo/4d3fc1ac61ed98d7a6eb1d8d9e6f7267.png'); background-size: cover; background-position: center;">
            <div class="absolute inset-0 bg-black/40 hover:bg-black/30 transition-colors"></div>
            <div class="relative z-10">
              <h3 class="text-xl font-semibold text-white">Нефтехимия</h3>
            </div>
          </a>

          <a href="/methods-eco" class="block relative rounded-lg p-6 border hover:shadow-lg transition-shadow overflow-hidden cursor-pointer" style="background-image: url('/home-photo/ecologylittle.png'); background-size: cover; background-position: center;">
            <div class="absolute inset-0 bg-black/40 hover:bg-black/30 transition-colors"></div>
            <div class="relative z-10">
              <h3 class="text-xl font-semibold text-white">Экология</h3>
            </div>
          </a>

          <a href="/methods-mining" class="block relative rounded-lg p-6 border hover:shadow-lg transition-shadow overflow-hidden cursor-pointer" style="background-image: url('/home-photo/gornlittle.png'); background-size: cover; background-position: center;">
            <div class="absolute inset-0 bg-black/40 hover:bg-black/30 transition-colors"></div>
            <div class="relative z-10">
              <h3 class="text-xl font-semibold text-white">Горнорудная промышленность</h3>
            </div>
          </a>

          <a href="/methods-metallurgy" class="block relative rounded-lg p-6 border hover:shadow-lg transition-shadow overflow-hidden cursor-pointer" style="background-image: url('/home-photo/metlittle.png'); background-size: cover; background-position: center;">
            <div class="absolute inset-0 bg-black/40 hover:bg-black/30 transition-colors"></div>
            <div class="relative z-10">
              <h3 class="text-xl font-semibold text-white">Металлургия</h3>
            </div>
          </a>

          <a href="/methods-diagnostics" class="block relative rounded-lg p-6 border hover:shadow-lg transition-shadow overflow-hidden cursor-pointer" style="background-image: url('/home-photo/diagnostikalittle2.png'); background-size: cover; background-position: center;">
            <div class="absolute inset-0 bg-black/40 hover:bg-black/30 transition-colors"></div>
            <div class="relative z-10">
              <h3 class="text-xl font-semibold text-white">Диагностика и контроль</h3>
            </div>
          </a>

          <!-- Геология -->
          <a href="/methods-geology" class="block relative rounded-lg p-6 border hover:shadow-lg transition-shadow overflow-hidden cursor-pointer" style="background-image: url('/home-photo/geologylittle.png'); background-size: cover; background-position: center;">
            <div class="absolute inset-0 bg-black/40 hover:bg-black/30 transition-colors"></div>
            <div class="relative z-10">
              <h3 class="text-xl font-semibold text-white">Геология</h3>
            </div>
          </a>

          <a href="/methods-research" class="block relative rounded-lg p-6 border hover:shadow-lg transition-shadow overflow-hidden cursor-pointer" style="background-image: url('/home-photo/researchlittle.png'); background-size: cover; background-position: center;">
            <div class="absolute inset-0 bg-black/40 hover:bg-black/30 transition-colors"></div>
            <div class="relative z-10">
              <h3 class="text-xl font-semibold text-white">Научные исследования</h3>
            </div>
          </a>

          <a href="/methods-gas" class="block relative rounded-lg p-6 border hover:shadow-lg transition-shadow overflow-hidden cursor-pointer" style="background-image: url('/home-photo/06bba93af58b01ffc5367e30d6485f7c.png'); background-size: cover; background-position: center;">
            <div class="absolute inset-0 bg-black/40 hover:bg-black/30 transition-colors"></div>
            <div class="relative z-10">
              <h3 class="text-xl font-semibold text-white">Газовая промышленность</h3>
            </div>
          </a>

        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
// Компонент не требует дополнительной логики
</script>