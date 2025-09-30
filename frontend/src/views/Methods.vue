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
           <MethodBlock
             v-for="method in methods"
             :key="method.title"
             :method="method"
           />
         </div>


       
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import MethodBlock from "@/components/MethodBlock.vue";

interface MethodItem {
  title: string;
  image: string;
  link: string;
  description: string;
  items: {
    text: string;
    image: string;
    link: string;
  }[];
}

const methods: MethodItem[] = [
  {
    title: "Методики анализа нефти и нефтепродуктов",
    image: "/home-photo/4d3fc1ac61ed98d7a6eb1d8d9e6f7267.png",
    link: "/methods-oil",
    description: "Анализ элементного состава нефти, бензина, дизельного топлива и других нефтепродуктов",
    items: [
      {
        text: "Анализ серы в нефтепродуктах",
        image: "/home-photo/4d3fc1ac61ed98d7a6eb1d8d9e6f7267.png",
        link: "/methods-oil"
      },
      {
        text: "Определение металлов в топливе",
        image: "/home-photo/4d3fc1ac61ed98d7a6eb1d8d9e6f7267.png",
        link: "/methods-oil"
      },
      {
        text: "Контроль качества бензина",
        image: "/home-photo/4d3fc1ac61ed98d7a6eb1d8d9e6f7267.png",
        link: "/methods-oil"
      }
    ]
  },
  {
    title: "Методики анализа в области экологии",
    image: "/home-photo/ecologylittle.png",
    link: "/methods-eco",
    description: "Анализ загрязняющих веществ в воде, почве, воздухе и отходах",
    items: [
      {
        text: "Анализ тяжелых металлов в воде",
        image: "/home-photo/ecologylittle.png",
        link: "/methods-eco"
      },
      {
        text: "Контроль загрязнения почвы",
        image: "/home-photo/ecologylittle.png",
        link: "/methods-eco"
      },
      {
        text: "Мониторинг атмосферных выбросов",
        image: "/home-photo/ecologylittle.png",
        link: "/methods-eco"
      }
    ]
  },
  {
    title: "Методики анализа в горнорудной промышленности",
    image: "/home-photo/gornlittle.png",
    link: "/methods-mining",
    description: "Анализ руд, минералов, горных пород и технологических продуктов",
    items: [
      {
        text: "Анализ рудных концентратов",
        image: "/home-photo/gornlittle.png",
        link: "/methods-mining"
      },
      {
        text: "Определение содержания металлов",
        image: "/home-photo/gornlittle.png",
        link: "/methods-mining"
      },
      {
        text: "Контроль качества минерального сырья",
        image: "/home-photo/gornlittle.png",
        link: "/methods-mining"
      }
    ]
  },
  {
    title: "Методики анализа в продукции металлургии",
    image: "/home-photo/metlittle.png",
    link: "/methods-metallurgy",
    description: "Анализ сплавов, металлов, ферросплавов и металлургических продуктов",
    items: [
      {
        text: "Анализ сталей и сплавов",
        image: "/home-photo/metlittle.png",
        link: "/methods-metallurgy"
      },
      {
        text: "Контроль ферросплавов",
        image: "/home-photo/metlittle.png",
        link: "/methods-metallurgy"
      },
      {
        text: "Определение примесей в металлах",
        image: "/home-photo/metlittle.png",
        link: "/methods-metallurgy"
      }
    ]
  },
  {
    title: "Методики анализа для диагностики и контроля",
    image: "/home-photo/diagnostikalittle2.png",
    link: "/methods-diagnostics",
    description: "Анализ износа, коррозии, смазочных материалов и технологических сред",
    items: [
      {
        text: "Диагностика износа двигателей",
        image: "/home-photo/diagnostikalittle2.png",
        link: "/methods-diagnostics"
      },
      {
        text: "Анализ коррозионных отложений",
        image: "/home-photo/diagnostikalittle2.png",
        link: "/methods-diagnostics"
      },
      {
        text: "Контроль смазочных материалов",
        image: "/home-photo/diagnostikalittle2.png",
        link: "/methods-diagnostics"
      }
    ]
  },
  {
    title: "Методики анализа в газовой промышленности",
    image: "/home-photo/06bba93af58b01ffc5367e30d6485f7c.png",
    link: "/methods-gas",
    description: "Анализ природного газа, углеводородов и газовых смесей",
    items: [
      {
        text: "Анализ состава природного газа",
        image: "/home-photo/06bba93af58b01ffc5367e30d6485f7c.png",
        link: "/methods-gas"
      },
      {
        text: "Определение серы в газе",
        image: "/home-photo/06bba93af58b01ffc5367e30d6485f7c.png",
        link: "/methods-gas"
      },
      {
        text: "Контроль качества углеводородов",
        image: "/home-photo/06bba93af58b01ffc5367e30d6485f7c.png",
        link: "/methods-gas"
      }
    ]
  }
];
</script>
