<script lang="ts" setup>
import { computed } from "vue";
import { useRouter, useRoute } from "vue-router";

import { useColorMode } from "@vueuse/core";
const mode = useColorMode();
mode.value = "dark";

// Роутер для умной навигации
const router = useRouter();
const route = useRoute();

import {
  NavigationMenu,
  NavigationMenuContent,
  NavigationMenuItem,
  NavigationMenuLink,
  NavigationMenuList,
  NavigationMenuTrigger,
} from "@/components/ui/navigation-menu";
import {
  Sheet,
  SheetContent,
  SheetFooter,
  SheetHeader,
  SheetTitle,
  SheetTrigger,
} from "@/components/ui/sheet";

import { Button } from "@/components/ui/button";
import { Separator } from "@/components/ui/separator";

import { Menu } from "lucide-vue-next";
import ToggleTheme from "./ToggleTheme.vue";

interface RouteProps {
  href: string;
  label: string;
}

interface FeatureProps {
  title: string;
  description: string;
  href?: string;
}

const routeList: RouteProps[] = [

  {
    href: "#hero",
    label: "Приборы",
  },
  {
    href: "#benefits",
    label: "Области применения",
  },
  {
    href: "#features",
    label: "О компании",
  },
  {
    href: "#team",
    label: "Методики",
  },


];

// Определяем, находимся ли мы на главной странице
const isHomePage = computed(() => route.path === '/');

// Метод для умной навигации
const handleNavigation = (href: string) => {
  if (isHomePage.value) {
    // На главной странице - используем якорные ссылки
    const element = document.querySelector(href);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  } else {
    // На других страницах - переходим на главную с якорем
    router.push(`/${href}`);
  }
};

const featureList: FeatureProps[] = [
  {
    title: "Анализаторы",
    description: "Современные аналитические приборы для точных измерений",
    href: "/analyzers",
  },
  {
    title: "Спектрометры",
    description: "Рентгенофлуоресцентные спектрометры для элементного анализа",
    href: "/spectrometers",
  },
];

import { ref } from "vue";

const isOpen = ref<boolean>(false);
</script>

<template>
  <header
    :class="{
      'shadow-light': mode === 'light',
      'shadow-dark': mode === 'dark',
      'w-full fixed top-0 left-0 right-0 border-b z-40 flex justify-between items-center px-4 py-3 bg-card shadow-md': true,
    }"
  >
    <a
      href="/"
      class="font-bold text-base sm:text-lg flex items-center"
    >
      <img 
        src="/logospectron-Photoroom.png" 
        alt="ООО СПЕКТРОН" 
        class="w-16 h-12 sm:w-20 sm:h-16 mr-2 rounded-lg object-contain"
      />
    </a>

    <!-- Mobile Navigation -->
    <div class="flex items-center gap-2 lg:hidden">
      <!-- Кнопки для мобильных -->
      <div class="flex items-center gap-1">
        <Button
          as-child
          size="sm"
          variant="ghost"
          class="p-2"
        >
          <router-link to="/profile">
            <span class="sr-only">Личный кабинет</span>
            <svg class="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
            </svg>
          </router-link>
        </Button>

        <ToggleTheme />

       
      </div>

      <Sheet v-model:open="isOpen">
        <SheetTrigger as-child>
          <Button variant="ghost" size="sm" class="p-2">
            <Menu class="h-5 w-5" />
          </Button>
        </SheetTrigger>

        <SheetContent
          side="right"
          class="flex flex-col bg-card w-[300px] sm:w-[400px]"
        >
          <SheetHeader class="mb-6">
            <SheetTitle class="flex items-center">
              <img 
                src="/logospectron-Photoroom.png" 
                alt="SPECTRON Logo" 
                class="w-12 h-10 mr-3 rounded-lg object-contain"
              />
              <span class="text-sm font-semibold">НПО "СПЕКТРОН"</span>
            </SheetTitle>
          </SheetHeader>

          <div class="flex-1 space-y-4">
            <!-- Приборы -->
            <div>
              <h3 class="text-sm font-semibold text-muted-foreground mb-3">Приборы</h3>
              <div class="space-y-2">
                <router-link
                  v-for="{ title, description, href } in featureList"
                  :key="title"
                  :to="href || '/'"
                  class="block p-3 rounded-lg hover:bg-muted transition-colors"
                  @click="isOpen = false"
                >
                  <p class="font-medium text-sm">{{ title }}</p>
                  <p class="text-xs text-muted-foreground mt-1">{{ description }}</p>
                </router-link>
              </div>
            </div>

            <Separator />

            <!-- Основная навигация -->
            <div>
          
              <div class="space-y-2">
                <button
                  v-for="{ href, label } in routeList"
                  :key="label"
                  class="block w-full text-left p-3 rounded-lg hover:bg-muted transition-colors text-sm"
                  @click="handleNavigation(href); isOpen = false"
                >
                  {{ label }}
                </button>
              </div>
            </div>
          </div>

          <SheetFooter class="mt-6 pt-4 border-t">
            <div class="space-y-3 w-full">
              <router-link
                to="/profile"
                class="flex items-center w-full p-3 rounded-lg hover:bg-muted transition-colors text-sm"
                @click="isOpen = false"
              >
                <svg class="h-4 w-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                </svg>
                Личный кабинет
              </router-link>

              <div class="flex items-center justify-between p-3">
                <span class="text-sm text-muted-foreground">Тема:</span>
                <ToggleTheme />
              </div>
            </div>
          </SheetFooter>
        </SheetContent>
      </Sheet>
    </div>

    <!-- Desktop -->
    <NavigationMenu class="hidden lg:block">
      <NavigationMenuList>
        <NavigationMenuItem>
          <NavigationMenuTrigger class="bg-card text-base">
            Приборы
          </NavigationMenuTrigger>
          <NavigationMenuContent>
            <div class="grid w-[400px] grid-cols-1 gap-3 p-4">
              <!-- <img
                src="/logospectron.png"
                alt="SPECTRON Logo"
                class="h-full w-full rounded-md object-cover"
              /> -->
              <ul class="flex flex-col gap-2">
                <li
                  v-for="{ title, description, href } in featureList"
                  :key="title"
                  class="rounded-md p-3 text-sm hover:bg-muted"
                >
                  <router-link 
                    v-if="href" 
                    :to="href" 
                    class="block"
                  >
                    <p class="mb-1 font-semibold leading-none text-foreground">
                      {{ title }}
                    </p>
                    <p class="line-clamp-2 text-muted-foreground">
                      {{ description }}
                    </p>
                  </router-link>
                  <div v-else>
                    <p class="mb-1 font-semibold leading-none text-foreground">
                      {{ title }}
                    </p>
                    <p class="line-clamp-2 text-muted-foreground">
                      {{ description }}
                    </p>
                  </div>
                </li>
              </ul>
            </div>
          </NavigationMenuContent>
        </NavigationMenuItem>

        <NavigationMenuItem>
          <NavigationMenuLink asChild>
            <Button
              v-for="{ href, label } in routeList"
              :key="label"
              as-child
              variant="ghost"
              class="justify-start text-base"
              @click="handleNavigation(href)"
            >
              <span>
                {{ label }}
              </span>
            </Button>
          </NavigationMenuLink>
        </NavigationMenuItem>
      </NavigationMenuList>
    </NavigationMenu>

    <div class="hidden lg:flex items-center gap-2">
      <Button
        as-child
        size="sm"
        variant="ghost"
        class="p-2"
      >
        <router-link to="/profile">
          <span class="sr-only">Личный кабинет</span>
          <svg class="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
          </svg>
        </router-link>
      </Button>

      <ToggleTheme />

      
    </div>
  </header>
</template>

<style scoped>
.shadow-light {
  box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.085);
}

.shadow-dark {
  box-shadow: inset 0 0 5px rgba(255, 255, 255, 0.141);
}
</style>
