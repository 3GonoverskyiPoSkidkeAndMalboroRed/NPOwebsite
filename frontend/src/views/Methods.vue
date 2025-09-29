<template>
  <div class="min-h-screen bg-background">
    <!-- Hero Section -->
    <section class="py-20 px-4 bg-gradient-to-b from-background to-muted/20">
      <div class="max-w-7xl mx-auto">
        <div class="text-center mb-16">
          <h1 class="text-4xl md:text-6xl font-bold mb-6 bg-gradient-to-r from-primary to-primary/70 bg-clip-text">
            Методики анализа элементного состава
          </h1>
        </div>

        <!-- Методики по отраслям -->
        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          <!-- Методики анализа нефти и нефтепродуктов -->
          <RouterLink
            to="/methods-oil"
            class="group block"
          >
            <Card class="h-full hover:shadow-xl transition-all duration-300 overflow-hidden cursor-pointer">
              <div class="relative h-48 overflow-hidden">
                <img
                  src="/home-photo/4d3fc1ac61ed98d7a6eb1d8d9e6f7267.png"
                  alt="Методики анализа нефти и нефтепродуктов"
                  class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300"
                />
                <div class="absolute inset-0 bg-black/30 group-hover:bg-black/20 transition-colors duration-300"></div>
                <div class="absolute inset-0 flex items-center justify-center">
                  <h3 class="text-2xl font-bold text-white text-center px-4">
                    Методики анализа нефти и нефтепродуктов
                  </h3>
                </div>
              </div>
              <CardHeader class="p-6">
                <CardTitle class="text-lg mb-2">Нефтехимия</CardTitle>
                <p class="text-muted-foreground text-sm">
                  Анализ элементного состава нефти, бензина, дизельного топлива и других нефтепродуктов
                </p>
              </CardHeader>
            </Card>
          </RouterLink>

          <!-- Методики анализа в области экологии -->
          <RouterLink
            to="/methods-eco"
            class="group block"
          >
            <Card class="h-full hover:shadow-xl transition-all duration-300 overflow-hidden cursor-pointer">
              <div class="relative h-48 overflow-hidden">
                <img
                  src="/home-photo/ecologylittle.png"
                  alt="Методики анализа в области экологии"
                  class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300"
                />
                <div class="absolute inset-0 bg-black/30 group-hover:bg-black/20 transition-colors duration-300"></div>
                <div class="absolute inset-0 flex items-center justify-center">
                  <h3 class="text-2xl font-bold text-white text-center px-4">
                    Методики анализа в области экологии
                  </h3>
                </div>
              </div>
              <CardHeader class="p-6">
                <CardTitle class="text-lg mb-2">Экология</CardTitle>
                <p class="text-muted-foreground text-sm">
                  Анализ загрязняющих веществ в воде, почве, воздухе и отходах
                </p>
              </CardHeader>
            </Card>
          </RouterLink>

          <!-- Методики анализа в горнорудной промышленности -->
          <RouterLink
            to="/methods-mining"
            class="group block"
          >
            <Card class="h-full hover:shadow-xl transition-all duration-300 overflow-hidden cursor-pointer">
              <div class="relative h-48 overflow-hidden">
                <img
                  src="/home-photo/gornlittle.png"
                  alt="Методики анализа в горнорудной промышленности"
                  class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300"
                />
                <div class="absolute inset-0 bg-black/30 group-hover:bg-black/20 transition-colors duration-300"></div>
                <div class="absolute inset-0 flex items-center justify-center">
                  <h3 class="text-2xl font-bold text-white text-center px-4">
                    Методики анализа в горнорудной промышленности
                  </h3>
                </div>
              </div>
              <CardHeader class="p-6">
                <CardTitle class="text-lg mb-2">Горнорудная промышленность</CardTitle>
                <p class="text-muted-foreground text-sm">
                  Анализ руд, минералов, горных пород и технологических продуктов
                </p>
              </CardHeader>
            </Card>
          </RouterLink>

          <!-- Методики анализа в продукции металлургии -->
          <RouterLink
            to="/methods-metallurgy"
            class="group block"
          >
            <Card class="h-full hover:shadow-xl transition-all duration-300 overflow-hidden cursor-pointer">
              <div class="relative h-48 overflow-hidden">
                <img
                  src="/home-photo/metlittle.png"
                  alt="Методики анализа в продукции металлургии"
                  class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300"
                />
                <div class="absolute inset-0 bg-black/30 group-hover:bg-black/20 transition-colors duration-300"></div>
                <div class="absolute inset-0 flex items-center justify-center">
                  <h3 class="text-2xl font-bold text-white text-center px-4">
                    Методики анализа в продукции металлургии
                  </h3>
                </div>
              </div>
              <CardHeader class="p-6">
                <CardTitle class="text-lg mb-2">Металлургия</CardTitle>
                <p class="text-muted-foreground text-sm">
                  Анализ сплавов, металлов, ферросплавов и металлургических продуктов
                </p>
              </CardHeader>
            </Card>
          </RouterLink>

          <!-- Методики анализа для диагностики и контроля -->
          <RouterLink
            to="/methods-diagnostics"
            class="group block"
          >
            <Card class="h-full hover:shadow-xl transition-all duration-300 overflow-hidden cursor-pointer">
              <div class="relative h-48 overflow-hidden">
                <img
                  src="/home-photo/diagnostikalittle2.png"
                  alt="Методики анализа для диагностики и контроля"
                  class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300"
                />
                <div class="absolute inset-0 bg-black/30 group-hover:bg-black/20 transition-colors duration-300"></div>
                <div class="absolute inset-0 flex items-center justify-center">
                  <h3 class="text-2xl font-bold text-white text-center px-4">
                    Методики анализа для диагностики и контроля
                  </h3>
                </div>
              </div>
              <CardHeader class="p-6">
                <CardTitle class="text-lg mb-2">Диагностика и контроль</CardTitle>
                <p class="text-muted-foreground text-sm">
                  Анализ износа, коррозии, смазочных материалов и технологических сред
                </p>
              </CardHeader>
            </Card>
          </RouterLink>

          <!-- Методики анализа в газовой промышленности -->
          <RouterLink
            to="/methods-gas"
            class="group block"
          >
            <Card class="h-full hover:shadow-xl transition-all duration-300 overflow-hidden cursor-pointer">
              <div class="relative h-48 overflow-hidden">
                <img
                  src="/home-photo/06bba93af58b01ffc5367e30d6485f7c.png"
                  alt="Методики анализа в газовой промышленности"
                  class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300"
                />
                <div class="absolute inset-0 bg-black/30 group-hover:bg-black/20 transition-colors duration-300"></div>
                <div class="absolute inset-0 flex items-center justify-center">
                  <h3 class="text-2xl font-bold text-white text-center px-4">
                    Методики анализа в газовой промышленности
                  </h3>
                </div>
              </div>
              <CardHeader class="p-6">
                <CardTitle class="text-lg mb-2">Газовая промышленность</CardTitle>
                <p class="text-muted-foreground text-sm">
                  Анализ природного газа, углеводородов и газовых смесей
                </p>
              </CardHeader>
            </Card>
          </RouterLink>
        </div>


       
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { Card, CardHeader, CardTitle } from "@/components/ui/card";
import { RouterLink } from "vue-router";
</script>
