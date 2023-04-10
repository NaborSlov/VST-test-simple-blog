import axios from "axios"


export default defineEventHandler(async (event) => {
    const formData = await readBody(event)
    const { webHost } = useRuntimeConfig()

    let url = `${webHost}/api/blogs/update/${formData.blog_id}/`

    try {
        const { data } = await axios({
            method: "patch",
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
        if (error.response !== undefined) {
            if (error.response.status === 403) {
                return { auth: false }
            }
        }
        return { error: error.message }
    }
})