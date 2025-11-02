from django.test import TestCase
from django.contrib.auth.models import User
from .models import Organizer, OrganizerUser, Customer


class OrganizerModelTest(TestCase):
    """Test cases for the Organizer model."""

    def setUp(self):
        self.organizer = Organizer.objects.create(
            name="Test Sports Event",
            contact_details="Phone: +358 123456789\nEmail: test@example.com",
            address="123 Test Street, Levi, Finland",
            description="A test sports event organizer"
        )

    def test_organizer_creation(self):
        """Test that an organizer can be created with required fields."""
        self.assertEqual(self.organizer.name, "Test Sports Event")
        self.assertIsNotNone(self.organizer.created_at)
        self.assertIsNotNone(self.organizer.updated_at)

    def test_organizer_str(self):
        """Test the string representation of an organizer."""
        self.assertEqual(str(self.organizer), "Test Sports Event")

    def test_organizer_unique_name(self):
        """Test that organizer names must be unique."""
        with self.assertRaises(Exception):
            Organizer.objects.create(
                name="Test Sports Event",
                contact_details="Different contact",
                address="Different address"
            )


class OrganizerUserModelTest(TestCase):
    """Test cases for the OrganizerUser model."""

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpass123"
        )
        self.organizer = Organizer.objects.create(
            name="Test Event",
            contact_details="Contact info",
            address="Test address"
        )

    def test_organizer_user_creation(self):
        """Test that an organizer-user relationship can be created."""
        org_user = OrganizerUser.objects.create(
            user=self.user,
            organizer=self.organizer,
            role='admin'
        )
        self.assertEqual(org_user.user, self.user)
        self.assertEqual(org_user.organizer, self.organizer)
        self.assertEqual(org_user.role, 'admin')

    def test_organizer_user_str(self):
        """Test the string representation of an organizer-user relationship."""
        org_user = OrganizerUser.objects.create(
            user=self.user,
            organizer=self.organizer,
            role='manager'
        )
        expected_str = f"{self.user.username} - {self.organizer.name} (manager)"
        self.assertEqual(str(org_user), expected_str)

    def test_organizer_user_unique_together(self):
        """Test that a user can only have one role per organizer."""
        OrganizerUser.objects.create(
            user=self.user,
            organizer=self.organizer,
            role='admin'
        )
        with self.assertRaises(Exception):
            OrganizerUser.objects.create(
                user=self.user,
                organizer=self.organizer,
                role='manager'
            )

    def test_multiple_roles_different_organizers(self):
        """Test that a user can have roles in multiple organizers."""
        organizer2 = Organizer.objects.create(
            name="Second Event",
            contact_details="Contact 2",
            address="Address 2"
        )
        org_user1 = OrganizerUser.objects.create(
            user=self.user,
            organizer=self.organizer,
            role='admin'
        )
        org_user2 = OrganizerUser.objects.create(
            user=self.user,
            organizer=organizer2,
            role='staff'
        )
        self.assertEqual(self.user.organizer_roles.count(), 2)


class CustomerModelTest(TestCase):
    """Test cases for the Customer model."""

    def setUp(self):
        self.user = User.objects.create_user(
            username="customer1",
            email="customer1@example.com",
            password="custpass123"
        )
        self.organizer = Organizer.objects.create(
            name="Event Organizer",
            contact_details="Contact details",
            address="Event address"
        )

    def test_customer_creation(self):
        """Test that a customer can be created."""
        customer = Customer.objects.create(
            user=self.user,
            organizer=self.organizer,
            notes="VIP customer"
        )
        self.assertEqual(customer.user, self.user)
        self.assertEqual(customer.organizer, self.organizer)
        self.assertEqual(customer.notes, "VIP customer")

    def test_customer_str(self):
        """Test the string representation of a customer."""
        customer = Customer.objects.create(
            user=self.user,
            organizer=self.organizer
        )
        expected_str = f"{self.user.username} - {self.organizer.name}"
        self.assertEqual(str(customer), expected_str)

    def test_customer_unique_together(self):
        """Test that a user can only be a customer once per organizer."""
        Customer.objects.create(
            user=self.user,
            organizer=self.organizer
        )
        with self.assertRaises(Exception):
            Customer.objects.create(
                user=self.user,
                organizer=self.organizer
            )

    def test_customer_multiple_organizers(self):
        """Test that a user can be a customer for multiple organizers."""
        organizer2 = Organizer.objects.create(
            name="Second Organizer",
            contact_details="Contact 2",
            address="Address 2"
        )
        customer1 = Customer.objects.create(
            user=self.user,
            organizer=self.organizer
        )
        customer2 = Customer.objects.create(
            user=self.user,
            organizer=organizer2
        )
        self.assertEqual(self.user.customer_profiles.count(), 2)
