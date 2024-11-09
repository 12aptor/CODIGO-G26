db.purchases.insertOne({
  customer: "John Doe",
  address: "123 Main St",
  total: 100,
  products: [
    {
      name: "iPhone 12",
      price: 999,
    },
    {
      name: "iPhone 12 Pro",
      price: 799,
    },
  ],
});
