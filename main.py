

class ShoppingCart:

    total = 0

    def __init__(self, tickets=[]):

        self.tickets = tickets
        self.promotions = [
            {'tickets_affected': ['OH'],
                'OH':{'adjustment_amount': -300,
                      'tickets_per_promotion': 3}
             },
            {'tickets_affected': ['BC'],
             'BC':{'adjustment_amount': -20, 'tickets_per_promotion': 4}
             }
        ]

        self.ticket_types = {
            'OH': 300,
            'BC': 110,
            'SK': 30}

        if tickets:
            self.calculate_total()
        else:
            print("add tickets")

    def add_ticket(self, ticket):
        self.tickets.append(ticket)
        self.calculate_total()

    def calculate_total(self):
        self.total = 0
        for ticket in self.tickets:
            self.total += self.ticket_types[ticket]
        self.apply_promotions()
        return self.total

    def apply_promotions(self):
        eligible_promotions = self.get_promotional_tickets()
        if eligible_promotions:
            for ticket in eligible_promotions:
                self.total += self.promotion_calculation(ticket)

    def promotion_calculation(self, ticket):
        quantity = sum(1 for x in self.tickets if x == ticket)
        #adjustment_amount =[]
        for promotion in self.promotions:
            if promotion['tickets_affected'][0] == ticket:
                adjustment_amount = promotion[ticket]['adjustment_amount']
                tickets_per_promotion = promotion[ticket]['tickets_per_promotion']
                break

        discount_multiplier = quantity // tickets_per_promotion
        return discount_multiplier * adjustment_amount

    def get_promotional_tickets(self):
        # return [promotion for promotion in self.promotions if promotion['tickets_affected'] in self.tickets]
        eligible_promotions = []
        for promotion in self.promotions:

            if promotion['tickets_affected'][0] in self.tickets:
                eligible_promotions.append(promotion['tickets_affected'][0])

        return eligible_promotions


class PromotionalRule:
    pass


class Ticket:
    pass


if __name__ == '__main__':
    cart = ShoppingCart()
    print(cart.total)
    cart.add_ticket('OH')
    cart.add_ticket('OH')
    cart.add_ticket('OH')
    print(cart.total)
