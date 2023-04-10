import axios from "axios"


export default defineEventHandler(async (event) => {
    const formData = await readBody(event)
    const { webHost } = useRuntimeConfig()

    let url = `${webHost}/api/blogs/`

    try {
        const { data } = await axios({
            method: "post",
            url: url,
            headers: {
                "cookie": `sessionid=${formData.cookie};csrftoken=${formData.csrf_token}`,
                "x-csrftoken": formData.csrf_token,
            },
            data: {
                title: formData.title,
                theme: formData.theme,
                description: formData.description
            },
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

