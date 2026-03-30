<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

const fullscreen = ref(false)

function onKey(e: KeyboardEvent) {
  if (e.key === 'Escape') fullscreen.value = false
}

onMounted(() => window.addEventListener('keydown', onKey))
onUnmounted(() => window.removeEventListener('keydown', onKey))
</script>

<template>
  <div class="cursor-pointer inline-block" @click="fullscreen = true">
    <slot />
  </div>
  <Teleport to="body">
    <div
      v-if="fullscreen"
      class="fixed inset-0 z-9999 flex items-center justify-center bg-black/90 cursor-pointer"
      @click="fullscreen = false"
    >
      <div class="max-w-3xl max-h-90vh overflow-auto p-8 text-white text-3xl leading-relaxed">
        <slot />
      </div>
    </div>
  </Teleport>
</template>
