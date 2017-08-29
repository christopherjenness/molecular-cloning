(ns molecular-cloning.core-test
  (:require [clojure.test :refer :all]
            [molecular-cloning.core :refer :all]))


(deftest codon-test
  (testing "Test codon hash-map"
    (is (= (molecular-cloning.core/codons "GGG") "Gly"))
    (is (= (molecular-cloning.core/codons "TAA") "TER"))))
