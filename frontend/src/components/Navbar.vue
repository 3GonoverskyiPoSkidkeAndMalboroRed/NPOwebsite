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
// import {
//   Sheet,
//   SheetContent,
//   SheetFooter,
//   SheetHeader,
//   SheetTitle,
//   SheetTrigger,
// } from "@/components/ui/sheet";

import { Button } from "@/components/ui/button";
// import { Separator } from "@/components/ui/separator";

// import { Menu } from "lucide-vue-next";
import GithubIcon from "@/icons/GithubIcon.vue";
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
  {
    href: "#faq",
    label: "ГОСТ",
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
    description:
      "Leverages social proof elements to establish trust and credibility.",
  },
  // {
  //   title: "Решаемые задачи",
  //   description:
  //     "Make your lead capture form visually appealing and strategically.",
  //   href: "/tasks",
  // },
  // {
  //   title: "Методики",
  //   description:
  //     "Make your lead capture form visually appealing and strategically.",
  // },
];

// const isOpen = ref<boolean>(false); // Удалено, так как мобильная навигация закомментирована
</script>

<template>
  <header
    :class="{
      'shadow-light': mode === 'light',
      'shadow-dark': mode === 'dark',
      'w-[90%] md:w-[70%] lg:w-[75%] lg:max-w-screen-xl top-5 mx-auto sticky border z-40 rounded-2xl flex justify-between items-center p-2 bg-card shadow-md': true,
    }"
  >
    <a
      href="/"
      class="font-bold text-lg flex items-center"
    >
      <img 
        src="/logospectron-Photoroom.png" 
        alt="ООО СПЕКТРОН" 
        class="w-20 h-16 mr-2 rounded-lg object-contain"
      />

    </a>

    <!-- Mobile
    <div class="flex items-center lg:hidden">
      <Sheet v-model:open="isOpen">
        <SheetTrigger as-child>
          <Menu
            @click="isOpen = true"
            class="cursor-pointer"
          />
        </SheetTrigger>

        <SheetContent
          side="left"
          class="flex flex-col justify-between rounded-tr-2xl rounded-br-2xl bg-card"
        >
          <div>
            <SheetHeader class="mb-4 ml-4">
              <SheetTitle class="flex items-center">
                <a
                  href="/"
                  class="flex items-center"
                >
                  <img 
                    src="/logospectron.png" 
                    alt="SPECTRON Logo" 
                    class="w-9 h-9 mr-2 rounded-lg object-contain"
                  />
                  Рентгеновские спектрометры и анализаторы
                </a>
              </SheetTitle>
            </SheetHeader>

            <div class="flex flex-col gap-2">
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
            </div>
          </div>

          <SheetFooter class="flex-col sm:flex-col justify-start items-start">
            <Separator class="mb-2" />

            <ToggleTheme />
          </SheetFooter>
        </SheetContent>
      </Sheet>
    </div> -->

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
        class="text-base"
      >
        <router-link to="/profile">
          Личный кабинет
        </router-link>
      </Button>

      <ToggleTheme />

      <Button
        as-child
        size="sm"
        variant="ghost"
        aria-label="View on GitHub"
      >
        <a
          aria-label="View on GitHub"
          href="https://github.com/leoMirandaa/shadcn-vue-landing-page.git"
          target="_blank"
        >
          <GithubIcon class="size-5" />
        </a>
      </Button>
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
