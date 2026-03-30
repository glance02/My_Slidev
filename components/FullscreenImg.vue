<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

const props = defineProps({
  src: { type: String, required: true },
  class: { type: String, default: '' },
})

const fullscreen = ref(false)

function open() {
  fullscreen.value = true
}

function close() {
  fullscreen.value = false
}

function onKey(e: KeyboardEvent) {
  if (e.key === 'Escape') close()
}

onMounted(() => window.addEventListener('keydown', onKey))
onUnmounted(() => window.removeEventListener('keydown', onKey))
</script>

<template>
  <img :src="src" :class="[$attrs.class, 'cursor-zoom-in']" @click="open" />
  <Teleport to="body">
    <div
      v-if="fullscreen"
      class="fixed inset-0 z-9999 flex items-center justify-center bg-black/90 cursor-zoom-out"
      @click="close"
    >
      <img :src="src" class="max-h-full max-w-full object-contain p-4" />
    </div>
  </Teleport>
</template>
