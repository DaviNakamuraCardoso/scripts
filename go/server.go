package main

import (
    "fmt"
    "log"
    "net/http"
)

func callback(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "Hello, World")
}

func main() {
    http.HandleFunc("/", callback)
    log.Fatal(http.ListenAndServe(":8080", nil))
}
