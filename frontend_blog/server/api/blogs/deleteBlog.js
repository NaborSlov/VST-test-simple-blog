import axios from "axios"


export default defineEventHandler(async (event) => {
    const formData = await readBody(event)
    const { webHost } = useRuntimeConfig()

    let url = `${webHost}/api/blogs/update/${formData.id}/`

    try {
        await axios({
            method: "delete",
            url: url,
            headers: {
                "cookie": `sessionid=${formData.cookie};csrftoken=${formData.csrf_token}`,
                "x-csrftoken": formData.csrf_token,
            },
        })
    }
    catch (error) {
        throw createError({statusCode: error.response.status, statusMessage: error.response.statusMessage})
    }

    return { status: "ok" }
})
