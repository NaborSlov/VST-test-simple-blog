import axios from "axios"


export default defineEventHandler(async (event) => {
    const { id } = getQuery(event)
    const { cookie } = await readBody(event)
    const { webHost } = useRuntimeConfig()

    let url = `${webHost}/api/blogs/`

    if (id) {
        url = url + id + '/'
    }


    try {
        const { data } = await axios({
            method: "get",
            url: url,
            headers: {
                "cookie": `sessionid=${cookie}`
            }
        })

        return { data: data, auth: true }
    }
    catch (error) {
        if (error.code === "ECONNREFUSED") {
            console.error(error);
            createError()  // написать ошибку под не работающий сервер
        } if (error.response.status === 403) {
            return { auth: false }
        }
        return { error: error.response }
    }
})

