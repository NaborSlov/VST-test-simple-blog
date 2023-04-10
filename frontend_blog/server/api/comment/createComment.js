import axios from "axios"


export default defineEventHandler(async (event) => {
    const formData = await readBody(event)
    const { webHost } = useRuntimeConfig()

    let url = `${webHost}/api/comment/`

    try {
        const { data } = await axios({
            method: "post",
            url: url,
            headers: {
                "cookie": `sessionid=${formData.cookie};csrftoken=${formData.csrf_token}`,
                "x-csrftoken": formData.csrf_token,
            },
            data: {
                blog: formData.id_blog,
                description: formData.comment
            },
        })

        return { data: data, auth: true }
    }
    catch (error) {
        if (error.response !== undefined) {
            if (error.response.status === 403) {
                return { auth: false }
            }
        }
        return { error: error.message }
    }

})