# Lab 6 — due Dec 1, 8 PM. Add 1e-16 before taking a log.
import math

def load_sequences(file):

    f = open(file, "r")
    lines = [x.strip() for x in f.readlines() if x.strip()]
    f.close()
    return lines


def compute_pwm(sequences):
    seq_len = len(sequences[0])

    pwm = {i:{x:0 for x in ["A", "T", "G", "C"]} for i in range(seq_len)}

    for seq in sequences:
        for idx, letter in enumerate(seq):
            pwm[idx][letter] += 1

    # normalize
    log_normalized = {x:{i:0.0 for i in range(seq_len)} for x in ["A", "T", "G", "C"]}

    for idx in range(seq_len):
        for letter in ["A", "T", "G", "C"]:
            log_normalized[letter][idx] = math.log2((pwm[idx][letter] / len(sequences)) / 0.25 + 1e-16)

    return log_normalized


def score_pwm(sequences, pwm):
    results = []

    for seq in sequences:
        log_prob = 0.0
        for idx, letter in enumerate(seq):
            log_prob += pwm[letter][idx]
        results.append(log_prob)

    return results
