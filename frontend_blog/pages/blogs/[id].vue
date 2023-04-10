<template>
    <main class="pt-8 pb-16 lg:pt-16 lg:pb-24 bg-white dark:bg-gray-900">
        <div class="flex justify-between px-4 mx-auto max-w-screen-xl ">
            <article
                class="mx-auto w-full max-w-2xl format format-sm sm:format-base lg:format-lg format-blue dark:format-invert">
                <header class="mb-4 lg:mb-6 not-format">
                    <address class="flex items-center mb-6 not-italic">
                        <div class="inline-flex items-center mr-3 text-sm text-gray-900 dark:text-white">
                            <div>
                                <a href="#" rel="author" class="text-xl font-bold text-gray-900 dark:text-white">{{
                                    response.data.author_name }}</a>
                                <p class="text-base font-light text-gray-500 dark:text-gray-400"><time pubdate
                                        datetime="2022-02-08" title="February 8th, 2022">{{ date }}</time></p>
                            </div>
                        </div>
                    </address>
                    <h1
                        class="mb-4 text-3xl font-extrabold leading-tight text-gray-900 lg:mb-6 lg:text-4xl dark:text-white">
                        {{ response.data.title }}</h1>
                </header>
                <p class="lead">{{ response.data.description }}</p>
                <section class="not-format">
                    <div class="flex justify-between items-center mb-6">
                        <h2 class="text-lg lg:text-2xl font-bold text-gray-900 dark:text-white">Комментарий ({{ response.data.comments.length }})</h2>
                    </div>
                    <form class="mb-6">
                        <div
                            class="py-2 px-4 mb-4 bg-white rounded-lg rounded-t-lg border border-gray-200 dark:bg-gray-800 dark:border-gray-700">
                            <label for="comment" class="sr-only">Your comment</label>
                            <textarea id="comment" rows="6"
                                class="px-0 w-full text-sm text-gray-900 border-0 focus:ring-0 dark:text-white dark:placeholder-gray-400 dark:bg-gray-800"
                                required></textarea>
                        </div>
                        <button type="submit"
                            class="inline-flex items-center py-2.5 px-4 text-xs font-medium text-center text-white bg-primary-700 rounded-lg focus:ring-4 focus:ring-primary-200 dark:focus:ring-primary-900 hover:bg-primary-800">
                            Добавить комментий
                        </button>
                    </form>
                    <div v-for="comment in response.data.comments">
                        <Comment :comment="comment"/>
                    </div>
                </section>
            </article>
        </div>
    </main>
</template>

<script setup>
const { id } = useRoute().params
const cookie = useCookie('sessionid')

const response = await $fetch(`/api/blogs/getBlog?id=${id}`, {  // Написать функцию сервера с получение одного
    method: 'post',
    body: {
        cookie: cookie.value
    }
})

if (response.auth === false) {
    navigateTo('/auth/')
} if (response.error) {
    createError()  // Написать страницу ошибок
}

let date = new Date(Date.parse(response.data.created))
date = date.toLocaleDateString('ru-RU', { day: 'numeric', month: 'numeric', year: 'numeric' })

</script>

<style scoped></style>
