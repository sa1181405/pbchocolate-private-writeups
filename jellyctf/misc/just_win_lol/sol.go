package main

import (
  "fmt"
  "math/rand"
  "time"
)

type card struct {
  value string
  suit  string
}

var cardValues = []string{"2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"}
var cardSuits = []string{"h", "c", "d", "s"}
var handSize = 12

func randHand(r rand.Rand) []card {
  hand := make([]card, handSize)
  sum := 0
  for sum < handSize {
    hand[sum] = card{
      value: cardValues[r.Intn(len(cardValues))],
      suit:  cardSuits[r.Intn(len(cardSuits))],
    }
    sum++
  }
  return hand
}

func isFiveOfAKind(hand []card) bool {
  counts := make(map[string]int)
  for _, card := range hand {
    element := card.value
    counts[element] = counts[element] + 1
    if counts[element] >= 5 {
      return true
    }
  }
  return false
}

func main() {
  var timeNow = time.Now().UTC().Unix()
  fmt.Println("timeNow: ", timeNow)
  for i:=0; i<30; i++ {
    for {
      timeNow++
      rand_time := rand.New(rand.NewSource(timeNow))
      hand := randHand(*rand_time)
      if isFiveOfAKind(hand) {
        fmt.Println(timeNow)
        break
      }
    }
  }
}
