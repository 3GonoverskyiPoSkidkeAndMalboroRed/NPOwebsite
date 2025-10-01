<script setup lang="ts">
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

interface MethodProps {
  title: string;
  description: string;
  code?: string;
}

const methodsList: MethodProps[] = [
  {
    title: "Определение элементов в почвах",
    description: "Определение элементов Mg, Al, Si, P, K, Ca, Ti, Mn, Fe, V, Cr, Co, Ni, Cu, Zn, As, Sr и Pb, а также оксидов элементов MgO, Al₂O₃, SiO₂, P₂O₅, K₂O, CaO, TiO₂, MnO, Fe₂O₃ в почвах",
    code: "ФР.1.31.2016.25423"
  },
  {
    title: "Анализ технологических водных сред АЭС",
    description: "Определение Ni, Cr, Mn и Co в технологических водных средах АЭС и жидких радиоактивных отходах",
    code: "ФР.1.31.2011.09282"
  },
  {
    title: "Анализ углей",
    description: "Определение S, P, K, Ca, Si, Cl, Mn, Fe, Ti и Sr в углях",
    code: "ФР.1.31.2014.17351"
  },
  {
    title: "Анализ водных сред АЭС",
    description: "Технологические водные среды атомных электростанций. Определение меди, железа, никеля, хрома, марганца, циркония, содержащихся в виде взвесей"
  },
  {
    title: "Анализ оловянных бронз",
    description: "Анализ оловянных бронз по ГОСТ 30608-98"
  }
];
</script>

<template>
  <section
    id="team"
    class="container px-4 sm:px-6 lg:px-8 py-16 sm:py-20 md:py-24 lg:py-32"
  >
    <div class="text-center mb-12 sm:mb-16">
      <h2 class="text-2xl sm:text-3xl md:text-4xl font-bold mb-4">
        Аттестованные методики анализа
      </h2>
    </div>

    <div class="grid gap-4 sm:gap-6 max-w-4xl mx-auto">
      <Card
        v-for="method in methodsList"
        :key="method.title"
        class="group hover:shadow-lg transition-all duration-300"
      >
        <CardHeader class="pb-3">
          <CardTitle class="text-lg sm:text-xl text-primary group-hover:text-primary/80 transition-colors">
            {{ method.title }}
          </CardTitle>
        </CardHeader>
        
        <CardContent>
          <p class="text-muted-foreground leading-relaxed mb-4 text-sm sm:text-base">
            {{ method.description }}
          </p>
          
          <div v-if="method.code" class="flex items-center justify-between">
            <span class="text-xs sm:text-sm font-mono bg-muted px-2 sm:px-3 py-1 rounded">
              {{ method.code }}
            </span>
          </div>
        </CardContent>
      </Card>
    </div>

    <div class="text-center mt-8 sm:mt-12">
      <a 
        href="/methods" 
        class="inline-flex items-center px-6 sm:px-8 py-3 sm:py-4 bg-primary text-primary-foreground rounded-lg hover:bg-primary/90 transition-colors font-medium text-base sm:text-lg">
        Все методики</a>
    </div>
  </section>
</template>
