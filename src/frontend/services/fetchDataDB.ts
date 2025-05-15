import { createClient } from "@libsql/client"

const turso = createClient({
  url: "libsql://tournaments-alexiiko.aws-eu-west-1.turso.io",
  authToken: "jeyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJhIjoicnciLCJnaWQiOiI4ODk2MzllYy0wMGVjLTQzNTMtYTgwYy02NWVmYjUwNGNiY2MiLCJpYXQiOjE3NDczMjI0NjEsInJpZCI6IjdjMmI5YTIyLTc3NTMtNDgwYS1hOGM5LWY1OTY1Yzk0ZGYwYiJ9.vXx_0xegrotXYpoHPcZ_Kiqfleaf7VfLXxOca-SMqJ9pASg2Yea5LL9yTNv8bK-d7wFc6st7EPpCpa200wOmCg"
})

const database = await turso.execute("SELECT * FROM M11")

console.log(database)
