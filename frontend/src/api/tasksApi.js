const API_BASE = import.meta.env.VITE_API_BASE || ''

async function request(path, options = {}) {
  const res = await fetch(`${API_BASE}${path}`, {
    headers: {
      'Content-Type': 'application/json',
      ...(options.headers || {})
    },
    ...options
  })

  if (res.status === 204) return null

  const data = await res.json().catch(() => null)
  if (!res.ok) {
    const message = data?.detail || `HTTP ${res.status}`
    throw new Error(message)
  }
  return data
}

export const tasksApi = {
  list() {
    return request('/api/tasks')
  },
  get(id) {
    return request(`/api/tasks/${id}`)
  },
  create(payload) {
    return request('/api/tasks', { method: 'POST', body: JSON.stringify(payload) })
  },
  update(id, payload) {
    return request(`/api/tasks/${id}`, { method: 'PUT', body: JSON.stringify(payload) })
  },
  remove(id) {
    return request(`/api/tasks/${id}`, { method: 'DELETE' })
  }
}
