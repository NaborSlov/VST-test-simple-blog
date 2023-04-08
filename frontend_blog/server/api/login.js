export default defineEventHandler(async (event) => {
    const { email, password } = await readBody(event)

    const { webHost } = useRuntimeConfig()

    const url = `http://${webHost}/user/login`

    // const { data } = await $fetch(url, {
    //     method: "post",
    //     body: {
    //         email: email,
    //         password: password,
    //     }
    // })

    const data = {message: "test"}

    return data
})
