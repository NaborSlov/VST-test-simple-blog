export default defineEventHandler(async (event) => {
    const { username, password } = await readBody(event)
    const { webHost } = useRuntimeConfig()

    await $fetch(`${webHost}/login/`, {
        method: "post",
        body: {
            username: username,
            password: password,
        }
    })
})
