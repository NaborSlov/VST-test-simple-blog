<template>
    <div class="flex justify-between items-center mb-5 text-gray-500">
        <span
            class="bg-primary-100 text-primary-800 text-xs font-medium inline-flex items-center px-2.5 py-0.5 rounded dark:bg-primary-200 dark:text-primary-800">
            <svg class="mr-1 w-3 h-3" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                <path
                    d="M2 6a2 2 0 012-2h6a2 2 0 012 2v8a2 2 0 01-2 2H4a2 2 0 01-2-2V6zM14.553 7.106A1 1 0 0014 8v4a1 1 0 00.553.894l2 1A1 1 0 0018 13V7a1 1 0 00-1.447-.894l-2 1z">
                </path>
            </svg>
            {{ blog.theme }}
        </span>
    </div>
    <NuxtLink :to="`/blogs/${blog.id}`">
        <h2 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white"><a href="#">{{ blog.title }}</a>
        </h2>
    </NuxtLink>
    <p class="mb-5 font-light text-gray-500 dark:text-gray-400">{{ blog.description }}</p>
    <div class="flex justify-between items-center">
        <div class="flex items-center space-x-4">
            <span class="font-medium dark:text-white">
                {{ blog.author_name }}
            </span>
        </div>
        <div class="flex items-start space-x-4">
            <NuxtLink :to="`/blogs/${blog.id}`">
                <p type="button"
                    class="text-white w-full inline-flex items-center justify-center bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800">
                    Подробнее
                </p>
            </NuxtLink>
            <NuxtLink :to="`/blogs/update?id=${blog.id}`">
                <button type="button"
                    class="text-white w-full inline-flex items-center justify-center bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800">
                    <svg aria-hidden="true" class="mr-1 -ml-1 w-5 h-5" fill="currentColor" viewBox="0 0 20 20"
                        xmlns="http://www.w3.org/2000/svg">
                        <path d="M17.414 2.586a2 2 0 00-2.828 0L7 10.172V13h2.828l7.586-7.586a2 2 0 000-2.828z"></path>
                        <path fill-rule="evenodd"
                            d="M2 6a2 2 0 012-2h4a1 1 0 010 2H4v10h10v-4a1 1 0 112 0v4a2 2 0 01-2 2H4a2 2 0 01-2-2V6z"
                            clip-rule="evenodd"></path>
                    </svg>
                    Редактировать
                </button>
            </NuxtLink>
            <button @click.prevent="delBlog(blog.id)"
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
    </div>
</template>

<script setup>
const { blog } = defineProps(['blog'])

async function delBlog(id) {
    const cookie = useCookie('sessionid').value
    const csrf_token = useCookie('csrftoken').value

    try {
        await $fetch("/api/blogs/deleteBlog", {
            method: "post",
            body: {
                id: id,
                cookie: cookie,
                csrf_token: csrf_token
            }
        })
    }
    catch (error) {
        throw createError({ statusMessage: error.statusMessage, statusCode: error.statusCode, fatal: true })
    }

    navigateTo('/', { external: true })
}

</script>

