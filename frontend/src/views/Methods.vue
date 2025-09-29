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
         <div class="space-y-12">
           <!-- Методики анализа нефти и нефтепродуктов -->
           <div class="bg-card rounded-lg border p-8 hover:shadow-lg transition-shadow">
             <div class="flex items-start gap-6">
               <div class="flex-shrink-0">
                 <img
                   src="/home-photo/4d3fc1ac61ed98d7a6eb1d8d9e6f7267.png"
                   alt="Нефтехимия"
                   class="w-24 h-24 object-cover rounded-lg"
                 />
               </div>
               <div class="flex-1">
                 <div class="flex items-center justify-between mb-4">
                   <h2 class="text-2xl font-bold text-primary">Методики анализа нефти и нефтепродуктов</h2>
                   <RouterLink
                     to="/methods-oil"
                     class="text-primary hover:text-primary/80 font-medium"
                   >
                     Подробнее →
                   </RouterLink>
                 </div>
                 <p class="text-muted-foreground mb-4">
                   Анализ элементного состава нефти, бензина, дизельного топлива и других нефтепродуктов
                 </p>
                 <ul class="space-y-2 text-sm">
                   <li class="flex items-center gap-2">
                     <span class="w-2 h-2 bg-primary rounded-full"></span>
                     Анализ серы в нефтепродуктах
                   </li>
                   <li class="flex items-center gap-2">
                     <span class="w-2 h-2 bg-primary rounded-full"></span>
                     Определение металлов в топливе
                   </li>
                   <li class="flex items-center gap-2">
                     <span class="w-2 h-2 bg-primary rounded-full"></span>
                     Контроль качества бензина
                   </li>
                 </ul>
               </div>
             </div>
           </div>

           <!-- Методики анализа в области экологии -->
           <div class="bg-card rounded-lg border p-8 hover:shadow-lg transition-shadow">
             <div class="flex items-start gap-6">
               <div class="flex-shrink-0">
                 <img
                   src="/home-photo/ecologylittle.png"
                   alt="Экология"
                   class="w-24 h-24 object-cover rounded-lg"
                 />
               </div>
               <div class="flex-1">
                 <div class="flex items-center justify-between mb-4">
                   <h2 class="text-2xl font-bold text-primary">Методики анализа в области экологии</h2>
                   <RouterLink
                     to="/methods-eco"
                     class="text-primary hover:text-primary/80 font-medium"
                   >
                     Подробнее →
                   </RouterLink>
                 </div>
                 <p class="text-muted-foreground mb-4">
                   Анализ загрязняющих веществ в воде, почве, воздухе и отходах
                 </p>
                 <ul class="space-y-2 text-sm">
                   <li class="flex items-center gap-2">
                     <span class="w-2 h-2 bg-primary rounded-full"></span>
                     Анализ тяжелых металлов в воде
                   </li>
                   <li class="flex items-center gap-2">
                     <span class="w-2 h-2 bg-primary rounded-full"></span>
                     Контроль загрязнения почвы
                   </li>
                   <li class="flex items-center gap-2">
                     <span class="w-2 h-2 bg-primary rounded-full"></span>
                     Мониторинг атмосферных выбросов
                   </li>
                 </ul>
               </div>
             </div>
           </div>

           <!-- Методики анализа в горнорудной промышленности -->
           <div class="bg-card rounded-lg border p-8 hover:shadow-lg transition-shadow">
             <div class="flex items-start gap-6">
               <div class="flex-shrink-0">
                 <img
                   src="/home-photo/gornlittle.png"
                   alt="Горнорудная промышленность"
                   class="w-24 h-24 object-cover rounded-lg"
                 />
               </div>
               <div class="flex-1">
                 <div class="flex items-center justify-between mb-4">
                   <h2 class="text-2xl font-bold text-primary">Методики анализа в горнорудной промышленности</h2>
                   <RouterLink
                     to="/methods-mining"
                     class="text-primary hover:text-primary/80 font-medium"
                   >
                     Подробнее →
                   </RouterLink>
                 </div>
                 <p class="text-muted-foreground mb-4">
                   Анализ руд, минералов, горных пород и технологических продуктов
                 </p>
                 <ul class="space-y-2 text-sm">
                   <li class="flex items-center gap-2">
                     <span class="w-2 h-2 bg-primary rounded-full"></span>
                     Анализ рудных концентратов
                   </li>
                   <li class="flex items-center gap-2">
                     <span class="w-2 h-2 bg-primary rounded-full"></span>
                     Определение содержания металлов
                   </li>
                   <li class="flex items-center gap-2">
                     <span class="w-2 h-2 bg-primary rounded-full"></span>
                     Контроль качества минерального сырья
                   </li>
                 </ul>
               </div>
             </div>
           </div>

           <!-- Методики анализа в продукции металлургии -->
           <div class="bg-card rounded-lg border p-8 hover:shadow-lg transition-shadow">
             <div class="flex items-start gap-6">
               <div class="flex-shrink-0">
                 <img
                   src="/home-photo/metlittle.png"
                   alt="Металлургия"
                   class="w-24 h-24 object-cover rounded-lg"
                 />
               </div>
               <div class="flex-1">
                 <div class="flex items-center justify-between mb-4">
                   <h2 class="text-2xl font-bold text-primary">Методики анализа в продукции металлургии</h2>
                   <RouterLink
                     to="/methods-metallurgy"
                     class="text-primary hover:text-primary/80 font-medium"
                   >
                     Подробнее →
                   </RouterLink>
                 </div>
                 <p class="text-muted-foreground mb-4">
                   Анализ сплавов, металлов, ферросплавов и металлургических продуктов
                 </p>
                 <ul class="space-y-2 text-sm">
                   <li class="flex items-center gap-2">
                     <span class="w-2 h-2 bg-primary rounded-full"></span>
                     Анализ сталей и сплавов
                   </li>
                   <li class="flex items-center gap-2">
                     <span class="w-2 h-2 bg-primary rounded-full"></span>
                     Контроль ферросплавов
                   </li>
                   <li class="flex items-center gap-2">
                     <span class="w-2 h-2 bg-primary rounded-full"></span>
                     Определение примесей в металлах
                   </li>
                 </ul>
               </div>
             </div>
           </div>

           <!-- Методики анализа для диагностики и контроля -->
           <div class="bg-card rounded-lg border p-8 hover:shadow-lg transition-shadow">
             <div class="flex items-start gap-6">
               <div class="flex-shrink-0">
                 <img
                   src="/home-photo/diagnostikalittle2.png"
                   alt="Диагностика и контроль"
                   class="w-24 h-24 object-cover rounded-lg"
                 />
               </div>
               <div class="flex-1">
                 <div class="flex items-center justify-between mb-4">
                   <h2 class="text-2xl font-bold text-primary">Методики анализа для диагностики и контроля</h2>
                   <RouterLink
                     to="/methods-diagnostics"
                     class="text-primary hover:text-primary/80 font-medium"
                   >
                     Подробнее →
                   </RouterLink>
                 </div>
                 <p class="text-muted-foreground mb-4">
                   Анализ износа, коррозии, смазочных материалов и технологических сред
                 </p>
                 <ul class="space-y-2 text-sm">
                   <li class="flex items-center gap-2">
                     <span class="w-2 h-2 bg-primary rounded-full"></span>
                     Диагностика износа двигателей
                   </li>
                   <li class="flex items-center gap-2">
                     <span class="w-2 h-2 bg-primary rounded-full"></span>
                     Анализ коррозионных отложений
                   </li>
                   <li class="flex items-center gap-2">
                     <span class="w-2 h-2 bg-primary rounded-full"></span>
                     Контроль смазочных материалов
                   </li>
                 </ul>
               </div>
             </div>
           </div>

           <!-- Методики анализа в газовой промышленности -->
           <div class="bg-card rounded-lg border p-8 hover:shadow-lg transition-shadow">
             <div class="flex items-start gap-6">
               <div class="flex-shrink-0">
                 <img
                   src="/home-photo/06bba93af58b01ffc5367e30d6485f7c.png"
                   alt="Газовая промышленность"
                   class="w-24 h-24 object-cover rounded-lg"
                 />
               </div>
               <div class="flex-1">
                 <div class="flex items-center justify-between mb-4">
                   <h2 class="text-2xl font-bold text-primary">Методики анализа в газовой промышленности</h2>
                   <RouterLink
                     to="/methods-gas"
                     class="text-primary hover:text-primary/80 font-medium"
                   >
                     Подробнее →
                   </RouterLink>
                 </div>
                 <p class="text-muted-foreground mb-4">
                   Анализ природного газа, углеводородов и газовых смесей
                 </p>
                 <ul class="space-y-2 text-sm">
                   <li class="flex items-center gap-2">
                     <span class="w-2 h-2 bg-primary rounded-full"></span>
                     Анализ состава природного газа
                   </li>
                   <li class="flex items-center gap-2">
                     <span class="w-2 h-2 bg-primary rounded-full"></span>
                     Определение серы в газе
                   </li>
                   <li class="flex items-center gap-2">
                     <span class="w-2 h-2 bg-primary rounded-full"></span>
                     Контроль качества углеводородов
                   </li>
                 </ul>
               </div>
             </div>
           </div>
         </div>


       
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { Card, CardHeader, CardTitle } from "@/components/ui/card";
import { RouterLink } from "vue-router";
</script>
