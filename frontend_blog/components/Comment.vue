<template>
    <article class="p-6 mb-6 ml-6 lg:ml-12 text-base bg-white rounded-lg dark:bg-gray-900">
        <footer class="flex justify-between items-center mb-2">
            <div class="flex items-center">
                <p class="inline-flex items-center mr-3 text-sm text-gray-900 dark:text-white">{{ comment.user.username }}
                </p>
                <p class="text-sm text-gray-600 dark:text-gray-400"><time pubdate datetime="2022-02-12"
                        title="February 12th, 2022">{{ date }}</time></p>
            </div>
            <div class="flex items-start space-x-4">
                <button @click.prevent="deleteComment(comment.id)"
                    class="inline-flex w-full items-center text-white justify-center bg-red-600 hover:bg-red-700 focus:ring-4 focus:outline-none focus:ring-red-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-red-500 dark:hover:bg-red-600 dark:focus:ring-red-900">
                    <svg aria-hidden="true" class="w-5 h-5 mr-1.5 -ml-1" fill="currentColor" viewBox="0 0 20 20"
                        xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd"
                            d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z"
                            clip-rule="evenodd"></path>
                    </svg>
                    Delete
                </button>

            </div>
        </footer>
        <p>{{ comment.description }}</p>
    </article>
</template>

<script setup>
const { comment } = defineProps(['comment'])

let date = new Date(Date.parse(comment.created))
date = date.toLocaleDateString('ru-RU', { day: 'numeric', month: 'numeric', year: 'numeric' })

async function deleteComment(id) {
    const cookie = useCookie('sessionid').value
    const csrf_token = useCookie('csrftoken').value
    const { path } = useRoute()

    const response = await $fetch("/api/comment/deleteComment", {
        method: "post",
        body: {
            id: id,
            cookie: cookie,
            csrf_token: csrf_token
        }
    })

    if (response.error) {
        throw createError({ statusMessage: response.error, statusCode: 404, fatal: true })
    }

    navigateTo(path, { external: true })
}

</script>
